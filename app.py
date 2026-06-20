import streamlit as st
import os
from main import process_video

st.title("AI Video Summarizer")

video = st.file_uploader(
    "Upload Video",
    type=["mp4", "avi", "mov"]
)

if video:

    st.video(video)

    os.makedirs("input", exist_ok=True)

    video_path = os.path.join("input", video.name)

    with open(video_path, "wb") as f:
        f.write(video.getbuffer())

    if st.button("Generate Summary"):

        with st.spinner("Generating Summary..."):
            summary = process_video(video_path)

        st.subheader("Summary")
        st.write(summary)