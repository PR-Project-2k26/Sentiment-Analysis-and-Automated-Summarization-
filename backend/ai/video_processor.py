import os

from ai.video_audio import extract_audio
from ai.video_transcriber import speech_to_text
from ai.video_summary import summarize_text


def process_video(video_path):

    os.makedirs("uploads/audio", exist_ok=True)

    audio_path = "uploads/audio/audio.wav"

    extract_audio(
        video_path,
        audio_path
    )

    transcript = speech_to_text(
        audio_path
    )

    if not transcript.strip():
        return {
            "transcript": "",
            "summary": "No speech detected."
        }

    summary = summarize_text(
        transcript
    )

    return {
        "transcript": transcript,
        "summary": summary
    }