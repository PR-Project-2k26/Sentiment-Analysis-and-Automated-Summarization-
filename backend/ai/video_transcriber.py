import whisper


def speech_to_text(audio_path):
    model = whisper.load_model("small")

    result = model.transcribe(
        audio_path,
        fp16=False
    )

    return result["text"]