# AI Text Summarizer


## Overview

AI Text Summarizer is an AI-powered web application that automatically generates concise, structured summaries from any piece of text. Beyond summarization, it analyzes sentiment, extracts key topics and keywords, and estimates readability — giving users a complete picture of a document without reading the whole thing.

This helps users quickly understand long articles, reports, or notes without reading the entire content.

## Features

* Paste any text for instant processing
* AI-generated summaries using Groq LLM, with adjustable length (Short / Medium / Long)
* Sentiment analysis combining the LLM's tone label with an independent VADER sentiment score
* Automatic key topic and keyword extraction
* Readability level detection (Beginner / Intermediate / Advanced)
* Text statistics — word counts, compression %, estimated reading time saved
* Auto-generated word cloud from extracted keywords
* Summary history with per-summary downloads
* Clean and user-friendly Streamlit interface
* Evaluation module for measuring summary quality (ROUGE score) and sentiment accuracy
* Command-line (CLI) mode for batch/file-based summarization

## 🛠️ Tech Stack

**Frontend**
* Streamlit

**Backend**
* Python

**AI & Machine Learning**
* Groq LLM (Llama 3.1 8B Instant)
* VADER Sentiment Analysis
* Natural Language Processing (NLP)

**Data & Visualization**
* WordCloud
* Matplotlib
* ROUGE Score (summary evaluation)

**Development Tools**
* Git & GitHub
* Streamlit

## Project Structure

```
Text-Summarizer/
│
├── input/                  # Sample input text (for CLI)
├── output/                 # CLI-generated summaries
├── eval/                   # Evaluation harness
│   ├── evaluate.py         # ROUGE + sentiment accuracy scoring
│   ├── test_data.json      # Labeled test samples
│   └── results.csv         # Generated after running evaluate.py
├── app.py                  # Streamlit UI
├── main.py                 # CLI summarization pipeline
├── utils.py                # Core logic — LLM calls, parsing, sentiment, stats, word cloud
├── requirements.txt        # Python dependencies
├── README.md                # Project documentation
└── .gitignore
```

## Installation

**1. Clone the Repository**
```
git clone https://github.com/PR-Project-2k26/Sentiment-Analysis-and-Automated-Summarization-.git
cd Sentiment-Analysis-and-Automated-Summarization-/Text-Summarizer
```

**2. Create Virtual Environment**
```
python -m venv .venv
```

**3. Activate Virtual Environment**

Windows
```
.venv\Scripts\activate
```

Linux / Mac
```
source .venv/bin/activate
```

**4. Install Dependencies**
```
pip install -r requirements.txt
```

**5. Configure Environment Variables**

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key
```

**6. Run the Application**
```
streamlit run app.py
```

## How It Works

1. User pastes text into the app and selects a summary length.
2. The text is sent to the Groq LLM, which returns a summary, tone, key topics, keywords, and readability level.
3. The text is separately scored for sentiment using VADER, as a second, independent signal.
4. Text statistics (word count, compression %, reading time) are computed locally.
5. A word cloud is generated from the extracted keywords.
6. Everything is displayed together in an interactive dashboard, with download and history options.

## Evaluation

Run `python eval/evaluate.py` to measure summary quality (ROUGE-1/2/L) and sentiment accuracy against a labeled test set. See `eval/test_data.json` for the reference samples.

## Author

Sparsh

## ⭐ Support

If you found this project useful, please consider giving it a Star ⭐ on GitHub.
