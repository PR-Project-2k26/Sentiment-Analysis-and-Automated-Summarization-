import re
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

_MODEL_ID = "sshleifer/distilbart-cnn-12-6"
_ENCODER_MAX = 1024
_CHUNK_CHAR_BUDGET = 3200

_tokenizer = AutoTokenizer.from_pretrained(_MODEL_ID)
_model = AutoModelForSeq2SeqLM.from_pretrained(_MODEL_ID)
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_model.to(_device)
_model.eval()

def _split_sentences(text: str) -> list[str]:
    text = (text or "").strip()
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip()]

def _chunk_transcript(text: str) -> list[str]:
    sentences = _split_sentences(text.replace("\r\n", "\n"))
    if not sentences:
        return []
    chunks: list[str] = []
    current: list[str] = []
    length = 0
    for sentence in sentences:
        add = len(sentence) + 1
        if current and length + add > _CHUNK_CHAR_BUDGET:
            chunks.append(" ".join(current))
            current = [sentence]
            length = add
        else:
            current.append(sentence)
            length += add
    if current:
        chunks.append(" ".join(current))
    return chunks

def _strip_summarization_artifacts(text: str) -> str:
    t = text.strip()
    for marker in ("\nBack to Mail", " Back to Mail", "\nBack to the page", "http://", "https://"):
        idx = t.find(marker)
        if idx != -1:
            t = t[:idx].strip()
    return t

def _generate_summary(
    passage: str, *, max_len: int, min_len: int, repetition_penalty: float = 1.12, no_repeat_ngram: int = 3
) -> str:
    inputs = _tokenizer(
        passage, max_length=_ENCODER_MAX, truncation=True, return_tensors="pt"
    )
    inputs = {k: v.to(_device) for k, v in inputs.items()}
    gen_kwargs = {
        "max_length": max_len, "min_length": min_len, "num_beams": 4,
        "length_penalty": 1.0, "repetition_penalty": repetition_penalty,
        "no_repeat_ngram_size": no_repeat_ngram, "early_stopping": True, "do_sample": False,
    }
    fbos = getattr(_model.generation_config, "forced_bos_token_id", None)
    if fbos is not None:
        gen_kwargs["forced_bos_token_id"] = fbos
        
    try:
        with torch.no_grad():
            summary_ids = _model.generate(**inputs, **gen_kwargs)
        decoded = _tokenizer.decode(summary_ids[0], skip_special_tokens=True).strip()
        return _strip_summarization_artifacts(decoded)
    except Exception as e:
        print(f"Warning: Failed to generate summary for a chunk. Error: {e}")
        return ""

def summarize_text(text: str) -> str:
    text = (text or "").strip()
    if not text:
        return ""

    chunks = _chunk_transcript(text)
    if not chunks:
        return ""

    # Map phase: Increased max_len and min_len to retain more key observations from each chunk
    partials = [
        _generate_summary(c, max_len=250, min_len=60) for c in chunks if c.strip()
    ]
    partials = [p for p in partials if p]
    
    if not partials:
        return "Summarization failed to generate valid text."

    if len(partials) == 1:
        return partials[0]

    # Reduce phase: Significantly increased lengths to allow a deeper, richer final summary
    merged_input = "\n\n".join(partials)
    return _generate_summary(
        merged_input, max_len=500, min_len=150, repetition_penalty=1.2, no_repeat_ngram=3
    )