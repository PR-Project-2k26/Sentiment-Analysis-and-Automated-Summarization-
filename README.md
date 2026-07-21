# Sentiment Analysis & Automated Summarization Platform

An AI-powered web application that combines multiple Natural Language Processing (NLP) and AI modules into a single platform. Users can analyze text sentiment, summarize text, audio, and video content, and evaluate resumes through one unified interface.

---

## Features

### Resume Analyzer
- ATS-friendly resume analysis
- Skill extraction
- Resume feedback and improvement suggestions

### Text Summarizer
- Summarize long articles and documents
- Preserve key information
- Fast AI-generated summaries

### Audio Summarizer
- Upload audio files
- Speech-to-text conversion
- AI-generated summaries

### Video Summarizer
- Upload video files
- Automatic audio extraction
- Speech transcription using OpenAI Whisper
- AI-powered summaries using Groq LLM

### Sentiment Analysis
- Classifies text as Positive, Neutral, or Negative
- Displays prediction confidence
- Useful for reviews, feedback, and social media analysis

---

# Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- Flask (Integration Layer)

## AI & Machine Learning
- OpenAI Whisper
- Groq LLM
- Hugging Face Transformers
- Natural Language Processing (NLP)

## Audio & Video Processing
- MoviePy
- FFmpeg

## Development Tools
- Git
- GitHub
- VS Code

---

# Project Structure

```text
Sentiment-Analysis-and-Automated-Summarization
│
├── frontend/
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── assets/
│
├── backend/
│
├── audio-summarizer/
├── text-summarizer/
├── video-summarizer/
├── resume-builder/
├── sentiment-analysis/
│
├── requirements.txt
└── README.md
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/PR-Project-2k26/Sentiment-Analysis-and-Automated-Summarization-.git
```

## Move to Project Directory

```bash
cd Sentiment-Analysis-and-Automated-Summarization-
```

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file and add your API keys.

```env
GROQ_API_KEY=your_api_key
```

## Run the Backend

```bash
python app.py
```

---

# Future Improvements

- User Authentication
- Dashboard for previous summaries
- Download summaries as PDF
- Multiple language support
- AI Chat Assistant
- Dark/Light Theme
- History Management
- Cloud Deployment

---

# Team Members

| Member | Module |
|---------|--------|
| Payal Choudhary | Resume Analyzer |
| Sparsh | Text Summarizer |
| Yash | Audio Summarizer |
| Bhavya Vaish | Video Summarizer |
| Team | Website Integration & Sentiment Analysis |
This project is developed for education---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
