import os
import streamlit as st
from pytube import YouTube

def download_video(url, output_dir):
    try:
        yt = YouTube(url)
        video_title = yt.title
        video = yt.streams.get_highest_resolution()
        video_path = os.path.join(output_dir, f"{video_title}.mp4")
        video.download(output_path=output_dir)
        return video_path, video_title
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
        return None, None

def main():
    st.title("Video URL Extractor and Downloader")

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
                    download_link = f'<a href="data:video/mp4;base64,{base64.b64encode(open(video_path, "rb").read()).decode()}">Download Video</a>'
                    st.markdown(download_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
