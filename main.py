import streamlit as st
from pytube import YouTube
import os


def download_video(url, output_dir):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video_title = video.title
        file_name = f"{video_title}.mp4"
        file_path = os.path.join(output_dir, file_name)
        if not os.path.exists(file_path):
            video.download(output_path=output_dir, filename=file_name)
        return file_path, video_title
    except:
        return None, None


def main():
    st.title("Video URL Extractor")

    # Get YouTube URL from user input
    url = st.text_input("Enter YouTube URL")

    if st.button("Extract Video URL", key="extract"):
        if url:
            with st.spinner("Extracting..."):
                output_dir = "output"
                os.makedirs(output_dir, exist_ok=True)
                video_path, video_title = download_video(url, output_dir)
            if video_path:
                if os.path.exists(video_path):
                    st.video(video_path)
                    file_size = os.path.getsize(video_path)
                    st.download_button(
                        label="Download Video",
                        data=open(video_path, "rb"),
                        file_name=video_title,
                        mime="video/mp4",
                        stats={
                            "file_size": file_size,
                            "file_name": video_title
                        }
                    )
                else:
                    st.error("Failed to download the video.")
            else:
                st.error("Failed to extract video URL.")


if __name__ == "__main__":
    main()
