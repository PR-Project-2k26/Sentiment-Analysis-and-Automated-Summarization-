from moviepy import VideoFileClip
import whisper

# Step 1: Extract Audio
def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    video.close()  # ✅ important to release file

# Step 2: Speech to Text
def speech_to_text(audio_path):
    model = whisper.load_model("base")
    
    # ✅ added fp16=False for CPU stability
    result = model.transcribe(audio_path, fp16=False)
    
    return result["text"]

# Step 3: Main Function
def process_video(video_path):
    audio_path = "output/audio.wav"

    print("Processing video...")

    # Extract audio
    extract_audio(video_path, audio_path)
    print("Audio extracted...")

    # Convert to text
    text = speech_to_text(audio_path)

    print("TEXT LENGTH:", len(text))

    print("\n--- TRANSCRIPT ---\n")
    print(text if text.strip() else "No speech detected ❌")

# Run
process_video("C:/Users/bhavy/Desktop/VideoSummarizer/input/test.mp4")