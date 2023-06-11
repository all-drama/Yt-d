import os
import streamlit as st
from pytube import YouTube

def get_yt_obj(url):
    try:
        obj = YouTube(url)
        return obj
    except:
        return None

def download_yt_video(video_url, output_dir, resolution):
    yt = get_yt_obj(video_url)
    if yt:
        st.subheader(f"Title: {yt.title}")
        st.image(yt.thumbnail_url, use_column_width=True)

        video_streams = yt.streams.filter(progressive=True, resolution=resolution).all()
        if not video_streams:
            st.warning(f"No video streams available for the selected resolution: {resolution}")
            return

        selected_stream = video_streams[0]

        st.markdown(f"**Downloading Video...**")
        video_path = selected_stream.download(output_path=output_dir)
        st.success(f"Video Downloaded: {video_path}")

        st.markdown(f"**Downloading Audio...**")
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_path = audio_stream.download(output_path=output_dir)
        st.success(f"Audio Downloaded: {audio_path}")

        st.markdown("**Merging Audio and Video...**")
        merged_path = os.path.join(output_dir, f"{yt.title}.mp4")
        os.system(f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a copy "{merged_path}"')
        st.success(f"Merged Video: {merged_path}")

        st.markdown(f"**Download Link:** [Download Merged Video]({merged_path})")

    else:
        st.warning("Please enter a valid YouTube Video URL")

def Main():
    st.set_page_config(layout="centered")
    st.header("YouTube Video Downloader")

    video_url = st.text_input("Enter YouTube Video URL")
    output_dir = st.text_input("Enter Output Directory", "./output")
    resolution = st.selectbox("Select Video Resolution", ["360p", "480p", "720p", "1080p"])

    if st.button("Download"):
        download_yt_video(video_url, output_dir, resolution)

if __name__ == "__main__":
    Main()
