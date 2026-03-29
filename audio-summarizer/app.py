from pathlib import Path

from transcribe import transcribe_audio
from summarize import summarize_text

# Resolve paths from this file’s folder so the app works no matter where you run Python from.
_PROJECT_ROOT = Path(__file__).resolve().parent

# Change only the path *inside* the project if your file lives elsewhere.
audio_path = _PROJECT_ROOT / "samples" / "audio.mp3"

if not audio_path.is_file():
    raise SystemExit(
        f"Audio file not found:\n  {audio_path}\n"
        "Place your audio there or update audio_path in app.py."
    )

transcript = transcribe_audio(str(audio_path))
summary = summarize_text(transcript)

transcript_path = audio_path.with_name(f"{audio_path.stem}_transcript.txt")
summary_path = audio_path.with_name(f"{audio_path.stem}_summary.txt")

transcript_path.write_text(transcript.strip() + "\n", encoding="utf-8")
summary_path.write_text(summary.strip() + "\n", encoding="utf-8")

print(f"\nTranscript saved to: {transcript_path.resolve()}")
print(f"Summary saved to:    {summary_path.resolve()}")

print("\n--- Summary ---\n")
print(summary)
