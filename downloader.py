import os
import re
import validators
from pytube import YouTube, Playlist, Channel
import streamlit as st
from tqdm import tqdm

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

    # Display resolution options
    resolution = st.selectbox("Select Video Resolution", resolutions, key="resolution_sele
                              ct")

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
