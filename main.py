import os
import re
import validators
from pytube import YouTube, Playlist, Channel
import streamlit as st
from tqdm import tqdm
import random

# Function for some random animations
def random_celeb():
    return random.choice([st.balloons()])

# Function to download YouTube single videos
def video(url):
    video_caller = YouTube(url)
    st.info(video_caller.title, icon="ℹ️")

    # Get available video streams
    streams = video_caller.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

    # Create a dictionary to store resolution and corresponding streams
    resolution_dict = {}
    for stream in streams:
        resolution = f"{stream.resolution} ({stream.mime_type.split('/')[1]})"
        resolution_dict[resolution] = stream

    # Get the available resolutions
    resolutions = list(resolution_dict.keys())

    # Display resolution options using HTML select element
    selected_resolution = st.empty()
    resolution = selected_resolution.selectbox("Select Video Resolution", resolutions, key="resolution_select", help="")

    # Find the selected stream based on the resolution string
    selected_stream = resolution_dict.get(resolution)

    if selected_stream is not None:
        st.info(f"Downloading video: {selected_stream.default_filename}")
        selected_stream.download()
        st.success('Done!')
        with open(selected_stream.default_filename, 'rb') as file:
            st.download_button('Download Video', file, file_name=selected_stream.default_filename + '.mp4')
    else:
        st.error('Oops! Stream is not available!')

# Function for downloading YouTube playlist
def playlist(url):
    playlist_obj = Playlist(url)
    st.info('Number of videos in playlist: %s' % len(playlist_obj.video_urls), icon="ℹ️")
    for video_url in tqdm(playlist_obj.video_urls, desc="Downloading playlist"):
        if validators.url(video_url):
            video(video_url)

# Function for downloading YouTube channel
def channel(url):
    channel_videos = Channel(url)
    st.info(f'Downloading videos by: {channel_videos.channel_name}', icon="ℹ️")
    for video_url in tqdm(channel_videos.video_urls, desc="Downloading channel"):
        if validators.url(video_url):
            video(video_url)

def main():
    st.title("YouTube Downloader")
    url = st.text_input(label="Paste your YouTube URL")
    download_button = st.button("Download")
    
    if download_button:
        if url:
            try:
                with st.spinner("Loading..."):
                    if 'playlist' in url:
                        playlist(url)
                    elif 'channel' in url:
                        channel(url)
                    else:
                        video(url)
                random_celeb()
            except Exception as e:
                st.error(e)
        st.experimental_rerun()

if __name__ == "__main__":
    main()
