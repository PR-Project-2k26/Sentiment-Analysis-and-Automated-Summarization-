# Audio Summarizer

Offline Speech-to-Text Transcription and Automated Summarization

This module takes an audio file (e.g., MP3, WAV), transcribes the spoken words into text using OpenAI's Whisper model, and generates a structured summary using a DistilBART language model.

## Key Features & How It Works
* **Offline Processing:** Does not require cloud APIs. All transcription and summarization happen locally on your machine.
* **Transcription (Whisper):** Uses the `medium` Whisper model for high-accuracy speech recognition. It automatically handles audio decoding via FFmpeg.
* **Summarization (DistilBART):** Processes long transcripts using a Map-Reduce chunking strategy to bypass token limits, retaining key observations and producing a comprehensive overview.
* **Automated Output:** Automatically generates separate `_transcript.txt` and `_summary.txt` files directly next to your input audio file.

## Prerequisites
Before installing the Python requirements, you must ensure **FFmpeg** is installed on your system for audio processing.
* **Windows:** The script attempts to fall back on `imageio-ffmpeg`, but installing FFmpeg globally via winget (`winget install ffmpeg`) is highly recommended.
* **Linux (Ubuntu/Debian):** `sudo apt install ffmpeg`
* **Mac:** `brew install ffmpeg`

## Installation Steps
We recommend running this project inside a Python Virtual Environment to prevent dependency conflicts with your system packages.

### 1. Setup the Virtual Environment
Open your terminal in the project directory and run:
```bash
python -m venv venv
```

### 2. Activate the Environment
* **Windows (Command Prompt):** `venv\Scripts\activate.bat`
* **Windows (PowerShell):** `venv\Scripts\Activate.ps1`
* **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies
Once activated, install the required packages (this will download PyTorch, Transformers, and Whisper):
```bash
pip install -r requirements.txt
```

## Usage
1. Place your target audio file into the `samples/` folder and name it `audio.mp3` (or update the `audio_path` variable inside `app.py` to point to your specific file).

2. Execute the main application script:
```bash
python app.py
```

Alternatively, on Windows, you can simply double-click the included `run.bat` file to automatically run the application.

### First Run Note
The very first time you execute the program, it will download the Whisper and DistilBART AI models to your local machine (several gigabytes). This will take a few minutes depending on your internet connection. Subsequent runs will be much faster.
