from moviepy.editor import VideoFileClip
import whisper
from groq import Groq
import os
from dotenv import load_dotenv

# -------------------------------
# LOAD ENVIRONMENT VARIABLES
# -------------------------------

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# -------------------------------
# GROQ CLIENT
# -------------------------------

client = Groq(api_key=api_key)

# -------------------------------
# EXTRACT AUDIO
# -------------------------------

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)

    video.audio.write_audiofile(
        audio_path,
        logger=None
    )

    video.close()

# -------------------------------
# SPEECH TO TEXT
# -------------------------------

def speech_to_text(audio_path):
    model = whisper.load_model("base")

    result = model.transcribe(
        audio_path,
        fp16=False
    )

    return result["text"]

# -------------------------------
# SUMMARIZE
# -------------------------------

def summarize_text(text):
    text = text.replace("\n", " ")
    text = text[:4000]

    prompt = f"""
You are an expert note maker.

Summarize the following transcript into structured bullet points.

IMPORTANT:
- Do NOT miss important details
- Include ALL key ideas
- Keep it clear and structured
- Use bullet points
- Avoid repetition

TEXT:
{text}

OUTPUT FORMAT:

Main Topic

Key Points

Important Details

Final Insight
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()

# -------------------------------
# FULL PIPELINE
# -------------------------------

def process_video(video_path):
    os.makedirs("output", exist_ok=True)

    audio_path = "output/audio.wav"

    extract_audio(video_path, audio_path)

    text = speech_to_text(audio_path)

    if not text.strip():
        return "No speech detected in the video."

    summary = summarize_text(text)

    with open(
        "output/summary.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(summary)

    return summary