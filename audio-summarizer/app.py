import sys
from pathlib import Path

from transcribe import transcribe_audio
from summarize import summarize_text

# Resolve paths from this file’s folder so the app works no matter where you run Python from.
_PROJECT_ROOT = Path(__file__).resolve().parent
_SAMPLES_DIR = _PROJECT_ROOT / "samples"

# Change only the path *inside* the project if your file lives elsewhere.
audio_path = _SAMPLES_DIR / "audio.mp3"

def main():
    if not audio_path.is_file():
        print(f"Error: Audio file not found at {audio_path}")
        print("Please place your audio there or update audio_path in app.py.")
        sys.exit(1)

    print(f"Transcribing {audio_path.name}...")
    try:
        transcript = transcribe_audio(str(audio_path))
    except Exception as e:
        print(f"Transcription failed: {e}")
        sys.exit(1)

    if not transcript or not transcript.strip():
        print("Error: No speech detected or transcription failed silently.")
        sys.exit(1)

    print("Summarizing transcript...")
    try:
        summary = summarize_text(transcript)
    except Exception as e:
        print(f"Summarization failed: {e}")
        sys.exit(1)

    # Save outputs to samples folder
    transcript_path = _SAMPLES_DIR / f"{audio_path.stem}_transcript.txt"
    summary_path = _SAMPLES_DIR / f"{audio_path.stem}_summary.txt"

    try:
        transcript_path.write_text(transcript.strip() + "\n", encoding="utf-8")
        summary_path.write_text(summary.strip() + "\n", encoding="utf-8")
    except IOError as e:
        print(f"Failed to save output files: {e}")
        sys.exit(1)

    print(f"\nTranscript saved to: {transcript_path.resolve()}")
    print(f"Summary saved to:    {summary_path.resolve()}")

    print("\n--- Summary ---\n")
    print(summary)

if __name__ == "__main__":
    main()