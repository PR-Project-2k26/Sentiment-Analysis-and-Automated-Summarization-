import shutil
import subprocess
from pathlib import Path

import numpy as np
import torch
import whisper

model = whisper.load_model("base")

_SAMPLE_RATE = 16000


def _ffmpeg_binary():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError as e:
        raise FileNotFoundError(
            "ffmpeg not found. Install FFmpeg and add it to PATH, or run: "
            "pip install imageio-ffmpeg"
        ) from e


def _load_audio_ffmpeg(file_path: str, sr: int = _SAMPLE_RATE) -> np.ndarray:
    """Decode audio to mono float32 PCM at ``sr`` Hz, same layout Whisper expects."""
    ffmpeg = _ffmpeg_binary()
    cmd = [
        ffmpeg,
        "-nostdin",
        "-threads",
        "0",
        "-i",
        str(Path(file_path).resolve()),
        "-f",
        "s16le",
        "-ac",
        "1",
        "-acodec",
        "pcm_s16le",
        "-ar",
        str(sr),
        "-",
    ]
    try:
        completed = subprocess.run(cmd, capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        stderr = e.stderr.decode(errors="replace") if e.stderr else ""
        raise RuntimeError(f"ffmpeg failed to decode audio: {stderr}") from e
    audio_i16 = np.frombuffer(completed.stdout, dtype=np.int16)
    return (audio_i16.astype(np.float32) / 32768.0).reshape(-1)


def transcribe_audio(file_path):
    waveform = _load_audio_ffmpeg(file_path)
    result = model.transcribe(waveform, fp16=model.device.type == "cuda")
    return result["text"]
