from moviepy import VideoFileClip

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)

    if video.audio is None:
        video.close()
        raise Exception("Uploaded video does not contain an audio track.")

    video.audio.write_audiofile(
        audio_path,
        logger=None
    )

    video.close()