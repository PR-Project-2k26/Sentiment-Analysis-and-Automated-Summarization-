from pathlib import Path

from transcribe import transcribe_audio
from summarize import summarize_text

audio_file = "samples/audio.mp3"

audio_path = Path(audio_file)
transcript = transcribe_audio(audio_file)
summary = summarize_text(transcript)

transcript_path = audio_path.with_name(f"{audio_path.stem}_transcript.txt")
summary_path = audio_path.with_name(f"{audio_path.stem}_summary.txt")

transcript_path.write_text(transcript.strip() + "\n", encoding="utf-8")
summary_path.write_text(summary.strip() + "\n", encoding="utf-8")

print(f"\nTranscript saved to: {transcript_path.resolve()}")
print(f"Summary saved to:    {summary_path.resolve()}")

print("\n--- Summary ---\n")
print(summary)
