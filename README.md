# Sentiment Analysis and Automated Summarization Platform

An AI-powered web application that combines multiple Natural Language Processing (NLP) and multimedia summarization tools into a single platform. The system enables users to analyze text sentiment and generate concise summaries from various content formats, including text, PDF documents, audio recordings, videos, and resumes.

---

## Features

- Resume Analysis
  - Resume parsing
  - ATS-friendly analysis
  - Skill extraction
  - Resume feedback

- PDF Summarizer
  - Upload PDF documents
  - Automatic text extraction
  - AI-generated summaries

- Text Summarizer
  - Paste text directly
  - Generate concise summaries
  - Preserve important information

- Audio Summarizer
  - Upload audio files
  - Speech-to-text conversion
  - AI-generated summary

- Video Summarizer
  - Upload video files
  - Audio extraction
  - Speech transcription (OpenAI Whisper)
  - AI-generated summaries (Groq LLM)
  - Streamlit interface

- Sentiment Analysis
  - Positive / Neutral / Negative prediction
  - Confidence score

---

## Tech Stack

### Frontend
- React.js
- HTML5
- CSS3
- JavaScript
- Streamlit (Video Module)

### Backend
- Node.js
- Express.js
- Python

### Database
- MongoDB

### AI / NLP
- Transformers
- Hugging Face
- OpenAI Whisper
- Groq LLM

### Other Tools
- FFmpeg
- MoviePy
- Git
- GitHub
- VS Code

---

## Project Structure

```text
Sentiment-Analysis-and-Automated-Summarization
│
├── audio-summarizer/
├── pdf-summarizer/
├── text-summarizer/
├── resume-builder/
├── video-summarizer/
└── ...
```

---

## Team Workflow

Each feature was developed independently in its own Git branch and later merged into `main`.

| Branch | Module |
|---------|---------|
| Resume-Builder | Resume Analyzer |
| PDF-Summarizer | PDF Summarizer |
| Text-Summarizer | Text Summarizer |
| Audio-Summarizer | Audio Summarizer |
| Video-Summarizer | Video Summarizer |

---

## Installation

```bash
git clone https://github.com/PR-Project-2k26/Sentiment-Analysis-and-Automated-Summarization-.git

cd Sentiment-Analysis-and-Automated-Summarization-

npm install
npm run dev
```

---

## Contributors

- Payal Choudhary – Resume Analyzer
- Sanidhya Digvijay – PDF Summarizer
- Sparsh – Text Summarizer
- Yash – Audio Summarizer
- Bhavya Vaish – Video Summarizer

---

⭐ If you found this project helpful, consider giving it a star.