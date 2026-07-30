from ai.model import model

def speech_to_text(audio_path):
    result = model.transcribe(
        audio_path,
        fp16=False
    )

    return result["text"]