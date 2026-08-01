# SummarAI - AI Powered Sentiment Analysis & Automated Summarization Platform

An AI-powered full-stack web application that combines multiple Natural Language Processing (NLP) and Artificial Intelligence modules into one platform. Users can summarize text, PDFs, audio, and video files, analyze resumes, perform sentiment analysis, and securely manage their processing history.

---

## Live Demo

### Frontend
https://sentiment-analysis-and-automated-su-six.vercel.app/

### Backend API
https://summarai-backend-drw7.onrender.com

---

# Features

## User Authentication

- User Registration
- Secure Login
- JWT Authentication
- Password Reset via Email
- Protected Routes

---

## Text Summarizer

- Summarize long text instantly
- AI-generated concise summaries
- Fast processing using Groq LLM

---

## PDF Summarizer

- Upload PDF documents
- Extract document text
- Generate intelligent summaries
- Preserve important information

---

## Audio Summarizer

- Upload audio files
- Speech-to-Text using OpenAI Whisper
- AI-generated summaries
- Supports multiple audio formats

---

## Video Summarizer

- Upload video files
- Automatic audio extraction using MoviePy
- Speech Transcription using OpenAI Whisper
- AI-generated summaries using Groq LLM

---

## Resume Analyzer

- ATS-Friendly Resume Analysis
- Skill Extraction
- Resume Score
- Personalized Improvement Suggestions

---

## Sentiment Analysis

- Detect Positive, Neutral, and Negative sentiments
- Confidence Prediction
- Useful for:
  - Customer Reviews
  - Social Media Posts
  - Feedback Analysis

---

## Dashboard

- Total Summaries
- Module-wise Statistics
- User Activity Overview
- History Analytics

---

## History Management

- Stores every processed summary
- View previous summaries
- Resume processing history
- Audio & Video history
- PDF history

---

# Tech Stack

## Frontend

- React.js
- Vite
- JavaScript
- HTML5
- CSS3
- Axios
- React Router DOM

---

## Backend

- Python
- Flask
- Flask JWT Extended
- Flask Mail
- Flask CORS

---

## Database

- MongoDB Atlas
- PyMongo

---

## Artificial Intelligence

- OpenAI Whisper
- Groq LLM
- Hugging Face Transformers
- NLP

---

## Audio & Video Processing

- MoviePy
- FFmpeg
- OpenAI Whisper

---

## Deployment

### Frontend

- Vercel

### Backend

- Render

### Database

- MongoDB Atlas

---

## Development Tools

- Git
- GitHub
- VS Code
- Postman

---

# Project Structure

```
Sentiment-Analysis-and-Automated-Summarization
│
├── backend/
│   ├── ai/
│   ├── config/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── uploads/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── assets/
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── .gitignore
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/PR-Project-2k26/Sentiment-Analysis-and-Automated-Summarization-.git
```

---

## 2. Move into Project

```bash
cd Sentiment-Analysis-and-Automated-Summarization-
```

---

# Backend Setup

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

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Backend Environment Variables

Create a `.env` file inside the backend folder.

```env
MONGO_URI=your_mongodb_connection_string

JWT_SECRET_KEY=your_secret_key

GROQ_API_KEY=your_groq_api_key

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your_email
MAIL_PASSWORD=your_app_password
MAIL_USE_TLS=True
```

---

## Run Backend

```bash
python app.py
```

Backend runs at

```
http://localhost:5000
```

---

# Frontend Setup

Move into frontend

```bash
cd frontend
```

Install dependencies

```bash
npm install
```

Create `.env`

```env
VITE_API_URL=http://localhost:5000/api
```

Run Frontend

```bash
npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# 🚀 Deployment

## Frontend

Deploy using **Vercel**

## Backend

Deploy using **Render**

## Database

MongoDB Atlas

---

# API Modules

- Authentication
- Dashboard
- History
- Resume Analyzer
- Text Summarizer
- PDF Summarizer
- Audio Summarizer
- Video Summarizer
- Sentiment Analysis

---

# Future Improvements

- AI Chat Assistant
- Multi-language Support
- Download Summary as PDF
- OCR Support
- Meeting Summarizer
- YouTube URL Summarizer
- Real-time Speech Summarization
- Admin Dashboard
- User Profile Management
- Theme Customization

---

# 👨‍💻 Team Members

| Member | Responsibility |
|---------|----------------|
| **Bhavya Vaish** | Video Summarizer, Full Stack Integration, Deployment, Backend Development |
| **Payal Choudhary** | Resume Analyzer |
| **Sparsh** | Text Summarizer |
| **Yash** | Audio Summarizer |
| **Entire Team** | Sentiment Analysis, Testing & Integration |

---

# Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# License

This project is developed for educational and learning purposes.

---

# ⭐Support

If you found this project useful,

⭐ Star this repository

Fork it

Contribute

---

## 💙 Built with AI, Python, Flask, React, MongoDB Atlas, Groq LLM, OpenAI Whisper & Vercel + Render
