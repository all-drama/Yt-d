import streamlit as st
from pytube import YouTube

def download_youtube_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        st.success("Download successful!")
    except Exception as e:
        st.error(f"Download failed: {str(e)}")

def main():
    st.title("YouTube Video Downloader")
    url = st.text_input("Enter YouTube video URL")
    if st.button("Download"):
        if url:
            download_youtube_video(url)
        else:
            st.warning("Please enter a YouTube video URL")

if __name__ == "__main__":
    main()
