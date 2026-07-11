import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import torch
import whisper

_SAMPLE_RATE = 16000
_model = None 

def _ffmpeg_binary():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError as e:
        py = sys.executable
        raise FileNotFoundError(
            "ffmpeg not found on PATH and the `imageio-ffmpeg` package is not installed."
        ) from e

def _load_audio_ffmpeg(file_path: str, sr: int = _SAMPLE_RATE) -> np.ndarray:
    ffmpeg = _ffmpeg_binary()
    cmd = [
        ffmpeg, "-nostdin", "-threads", "0", "-i", str(Path(file_path).resolve()),
        "-f", "s16le", "-ac", "1", "-acodec", "pcm_s16le", "-ar", str(sr), "-"
    ]
    try:
        completed = subprocess.run(cmd, capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        stderr = e.stderr.decode(errors="replace") if e.stderr else ""
        raise RuntimeError(f"ffmpeg failed to decode audio: {stderr}") from e
    
    if not completed.stdout:
        raise RuntimeError("ffmpeg returned no audio data. The file may be empty or corrupted.")
        
    audio_i16 = np.frombuffer(completed.stdout, dtype=np.int16)
    return (audio_i16.astype(np.float32) / 32768.0).reshape(-1)

def transcribe_audio(file_path):
    global _model
    if _model is None:
        # Upgraded from "base" to "medium" for much higher accuracy
        _model = whisper.load_model("medium")
        
    waveform = _load_audio_ffmpeg(file_path)
    result = _model.transcribe(waveform, fp16=_model.device.type == "cuda")
    return result["text"]