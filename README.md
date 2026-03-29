# Sentiment-Analysis-and-Automated-Summarization-

Audio → **transcript** (plain text) → **summary**, with both results saved as `.txt` files next to the source audio.

## What it does

1. **Transcription** — Decodes the audio file with **FFmpeg**, then runs **OpenAI Whisper** (`base` model) to turn speech into text.
2. **Summarization** — Feeds that transcript to **DistilBART** (`sshleifer/distilbart-cnn-12-6`) using a **map → reduce** pattern so long recordings are summarized reliably (see below).
3. **Outputs** — Writes UTF-8 text files in the **same folder as the input audio**:
   - `{stem}_transcript.txt` — full transcript  
   - `{stem}_summary.txt` — summary  

Example: if the input is `samples/audio.mp3`, you get `samples/audio_transcript.txt` and `samples/audio_summary.txt`.

## How the code is structured

| File | Role |
|------|------|
| `app.py` | Entry point: loads audio path, calls transcribe + summarize, saves `.txt` files, prints the summary. |
| `transcribe.py` | Locates **FFmpeg** (system `PATH` or **`imageio-ffmpeg`** bundle), decodes audio to 16 kHz mono float32, runs **Whisper** on that waveform, returns a string. Uses FP16 on GPU only (FP32 on CPU). |
| `summarize.py` | Loads **DistilBART** once. Splits the transcript into sentence-based **chunks** (~3200 characters each, within the model’s encoder limit). Summarizes each chunk, then **merges** those partial summaries into one final summary when there are multiple chunks. Strips common training-data boilerplate from the decoded text when it appears. |

### Why chunked summarization?

One neural summarizer can only take a **limited amount of text** at once (here, up to **1024** subword tokens per pass). Long transcripts would be cut off if summarized in a single call. Chunking summarizes **every part** of the transcript; the second pass **reduces** overlapping partial summaries into a single overview.

## Setup

- **Python 3** (project tested with a recent 3.x; use a virtual environment recommended).
- **PyTorch** — install a build that matches your machine ([PyTorch install guide](https://pytorch.org/get-started/locally/)). CPU works; GPU speeds up Whisper and the summarizer.
- **FFmpeg** — Either install FFmpeg and add it to `PATH`, or rely on **`imageio-ffmpeg`** (listed in `requirements.txt`), which ships a binary used when `ffmpeg` is not on the path.

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
```

First run may **download** Whisper weights and the Hugging Face summarizer; ensure you have network access. Optional: set `HF_TOKEN` for higher Hugging Face Hub rate limits.

## Run

1. Put your audio where you want (e.g. under `samples/`), or change the path in `app.py`.
2. Set `audio_file` in `app.py` if needed (default: `samples/audio.mp3`).
3. Execute:

```bash
python app.py
```

Check the printed paths for the saved `.txt` files.

## Limitations (good to know)

- **Summary quality** follows **transcript quality** — misheard words or wrong segments from Whisper will carry into the summary.
- The summarizer is **abstractive** (it rephrases) but tuned for **news-style** text; very unusual speech may still produce imperfect wording.
- **VRAM / RAM**: larger Whisper models and GPU help on long files; DistilBART is relatively light.

## Requirements

See `requirements.txt` for packages: `openai-whisper`, `imageio-ffmpeg`, `transformers`, `torch`.
