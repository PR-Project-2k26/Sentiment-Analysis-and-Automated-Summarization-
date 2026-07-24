from ai.video_transcriber import speech_to_text
from ai.video_summary import summarize_text


def process_audio(audio_path):
    transcript = speech_to_text(audio_path)

    if not transcript.strip():
        return {
            "transcript": "",
            "summary": "No speech detected."
        }

    summary = summarize_text(transcript)

    return {
        "transcript": transcript,
        "summary": summary
    }