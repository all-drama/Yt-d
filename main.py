import random
import streamlit as st
from pytube import YouTube, Playlist, Channel
from tqdm import tqdm

# Function for the balloon animation
def balloon_animation():
    st.balloons()

# Function to download YouTube single videos
def video(url):
    video_caller = YouTube(url)
    st.info(video_caller.title, icon="ℹ️")

    # Get available video streams
    video_streams = video_caller.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

    # Get available audio streams
    audio_streams = video_caller.streams.filter(only_audio=True).order_by('abr').desc()

    # Create a dictionary to store resolution and corresponding video streams
    video_options = {}
    for stream in video_streams:
        resolution = f"{stream.resolution} ({stream.mime_type.split('/')[1]})"
        video_options[resolution] = stream

    # Create a dictionary to store audio and corresponding audio streams
    audio_options = {}
    for stream in audio_streams:
        audio_format = f"Audio ({stream.abr} {stream.mime_type.split('/')[1]})"
        audio_options[audio_format] = stream

    # Get the available video resolutions and audio options
    video_resolutions = list(video_options.keys())
    audio_formats = list(audio_options.keys())

    # Display video resolutions and audio options
    resolution = st.selectbox("Select Video Resolution", video_resolutions, index=0)
    audio_option = st.selectbox("Select Audio Option", audio_formats, index=0)

    # Find the selected video stream based on the resolution
    selected_video_stream = video_options.get(resolution)

    # Find the selected audio stream based on the audio option
    selected_audio_stream = audio_options.get(audio_option)

    if selected_video_stream is not None and selected_audio_stream is not None:
        st.info(f"Downloading video: {selected_video_stream.default_filename}")
        video_progress_bar = st.progress(0)
        video_progress_text = st.empty()
        video_stream = selected_video_stream.stream_to_buffer(progressive=True)
        with open(selected_video_stream.default_filename, 'wb') as file:
            with tqdm(total=selected_video_stream.filesize, unit='bytes', unit_scale=True) as progress_bar:
                for chunk in video_stream.iter_content(chunk_size=1024):
                    file.write(chunk)
                    progress_bar.update(len(chunk))
                    video_progress_bar.progress(progress_bar.n / progress_bar.total)
                    video_progress_text.text(f"Progress: {progress_bar.n}/{progress_bar.total} bytes")
        st.success('Video Downloaded!')

        st.info(f"Downloading audio: {selected_audio_stream.default_filename}")
        audio_progress_bar = st.progress(0)
        audio_progress_text = st.empty()
        audio_stream = selected_audio_stream.stream_to_buffer()
        with open(selected_audio_stream.default_filename, 'wb') as file:
            with tqdm(total=selected_audio_stream.filesize, unit='bytes', unit_scale=True) as progress_bar:
                for chunk in audio_stream.iter_content(chunk_size=1024):
                    file.write(chunk)
                    progress_bar.update(len(chunk))
                    audio_progress_bar.progress(progress_bar.n / progress_bar.total)
                    audio_progress_text.text(f"Progress: {progress_bar.n}/{progress_bar.total} bytes")
        st.success('Audio Downloaded!')

        with open(selected_video_stream.default_filename, 'rb') as file:
            st.download_button('Download Video', file, file_name=selected_video_stream.default_filename + '.mp4')

        with open(selected_audio_stream.default_filename, 'rb
    else:
        st.error('Oops! Stream is not available!')

# Function to download YouTube playlist
def playlist(url):
    playlist_obj = Playlist(url)
    st.info('Number of videos in playlist: %s' % len(playlist_obj.video_urls), icon="ℹ️")

    for video_url in playlist_obj.video_urls:
        try:
            video(video_url)
        except Exception as e:
            st.error(f"Error downloading video: {video_url}")
            st.error(e)

# Function to download YouTube channel
def channel(url):
    channel_videos = Channel(url)
    st.info(f'Downloading videos by: {channel_videos.channel_name}', icon="ℹ️")

    for video in channel_videos.videos:
        try:
            video_url = video.watch_url
            video(video_url)
        except Exception as e:
            st.error(f"Error downloading video: {video_url}")
            st.error(e)

# Integration of all above-defined functions
st.title("YouTube Downloader")
url = st.text_input(label="Paste your YouTube URL")
if st.button("Download"):
    if url:
        try:
            with st.spinner("Loading..."):
                if 'playlist' in url:
                    playlist(url)
                elif 'channel' in url:
                    channel(url)
                else:
                    video(url)
            balloon_animation()
        except Exception as e:
            st.error(e)
            