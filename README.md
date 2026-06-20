# AI Video Summarizer

🔗 **Live Demo:** https://video-summarizer-qjnjtkgtzm6ydfe28ccp6t.streamlit.app/

## Overview

AI Video Summarizer is an AI-powered web application that automatically generates concise summaries from video content. The application extracts audio from uploaded videos, converts speech into text using OpenAI Whisper, and generates structured summaries using Groq LLMs.

This helps users quickly understand long videos without watching the entire content.

---

## Features

* Upload video files for processing
* Automatic audio extraction using FFmpeg & MoviePy
* Speech-to-text transcription using OpenAI Whisper
* AI-generated summaries using Groq LLM
* Fast and efficient processing pipeline
* Clean and user-friendly Streamlit interface
* Supports long-form video content
* Downloadable summary output

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & Machine Learning

* OpenAI Whisper
* Groq LLM (Llama 3.3 70B Versatile)
* Natural Language Processing (NLP)

### Video Processing

* MoviePy
* FFmpeg

### Development Tools

* Git & GitHub

---

## Project Structure

```text
Video-Summarizer/
│
├── input/                  # Uploaded videos
├── output/                 # Extracted audio & summaries
├── app.py                  # Streamlit UI
├── main.py                 # Video processing pipeline
├── requirements.txt        # Python dependencies
├── packages.txt            # System dependencies (FFmpeg)
├── README.md               # Project documentation
└── .gitignore
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/bstar042005/Video-Summarizer.git
cd Video-Summarizer
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install FFmpeg

Download FFmpeg and add it to your system PATH.

Verify installation:

```bash
ffmpeg -version
```

### 6. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### 7. Run the Application

```bash
streamlit run app.py
```

---

## How It Works

1. User uploads a video.
2. Audio is extracted using MoviePy.
3. OpenAI Whisper converts speech into text.
4. Transcript is sent to Groq LLM.
5. AI generates a structured summary.
6. Summary is displayed to the user.

---

## Live Demo

https://video-summarizer-qjnjtkgtzm6ydfe28ccp6t.streamlit.app/

---

## Future Improvements

* Multi-language transcription
* Speaker identification
* PDF summary export
* Timestamp-based summaries
* YouTube video summarization
* Custom summary lengths
* Topic-wise chapter generation

---

## Author

**Bhavya Vaish**

## ⭐ Support

If you found this project useful, please consider giving it a **Star ⭐** on GitHub.
