import streamlit as st
import os
from main import process_video

st.set_page_config(
    page_title="AI Video Summarizer",
    page_icon="🎥"
)

st.title("AI Video Summarizer")
st.write("Upload a video and get an AI-generated summary.")

video = st.file_uploader(
    "Upload Video",
    type=["mp4", "avi", "mov", "mkv"]
)

if video:

    st.success("Video Uploaded Successfully!")

    st.video(video)

    os.makedirs("input", exist_ok=True)

    video_path = os.path.join("input", video.name)

    with open(video_path, "wb") as f:
        f.write(video.getbuffer())

    if st.button("Generate Summary"):

        with st.spinner("Processing Video..."):

            try:
                summary = process_video(video_path)

                st.subheader("Summary")
                st.write(summary)

            except Exception as e:
                st.error(f"Error: {str(e)}")