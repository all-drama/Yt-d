import random
import streamlit as st
from pytube import YouTube, Playlist, Channel

# List of available animations
animations = [
    "🎉",
    "🎊",
    "🥳",
    "🎇",
    "🎆",
    "✨",
    "🌟",
    "🎈",
    "🎁",
    "🎵",
]

# Function for a random animation
def random_celeb():
    random_animation = random.choice(animations)
    st.success(random_animation)

# Function to download YouTube single videos
def video(url):
    video_caller = YouTube(url)
    st.info(video_caller.title, icon="ℹ️")

    # Get available video streams
    streams = video_caller.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    audio_streams = video_caller.streams.filter(only_audio=True).order_by('abr').desc()

    # Create a dictionary to store resolution and corresponding streams
    resolution_dict = {}
    for stream in streams:
        resolution = f"{stream.resolution} ({stream.mime_type.split('/')[1]})"
        resolution_dict[resolution] = stream

    # Create a dictionary to store audio and corresponding streams
    audio_dict = {}
    for stream in audio_streams:
        audio_format = f"Audio ({stream.abr} {stream.mime_type.split('/')[1]})"
        audio_dict[audio_format] = stream

    # Get the available resolutions and audio options
    resolutions = list(resolution_dict.keys())
    audio_options = list(audio_dict.keys())

    # Display resolution and audio options
    resolution = st.selectbox("Select Video Resolution", resolutions, index=0)
    audio_option = st.selectbox("Select Audio Option", audio_options, index=0)

    # Find the selected stream based on the resolution and audio option
    selected_stream = resolution_dict.get(resolution)
    selected_audio = audio_dict.get(audio_option)

    if selected_stream is not None and selected_audio is not None:
        st.info(f"Downloading video: {selected_stream.default_filename}")
        selected_stream.download()
        st.success('Done!')

        st.info(f"Downloading audio: {selected_audio.default_filename}")
        selected_audio.download()
        st.success('Done!')

        with open(selected_stream.default_filename, 'rb') as file:
            st.download_button('Download Video', file, file_name=selected_stream.default_filename + '.mp4')

        with open(selected_audio.default_filename, 'rb') as file:
            st.download_button('Download Audio', file, file_name=selected_audio.default_filename + '.mp3')

    else:
        st.error('Oops! Stream is not available!')

# Function to download YouTube playlist
def playlist(url):
    playlist_obj = Playlist(url)
    st.info('Number of videos in playlist: %s' % len(playlist_obj.video_urls), icon="ℹ️")
    for video in playlist_obj.videos:
        x = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if x is not None:
            x.download()
            st.success('Done!')
            with open(x.default_filename, 'rb') as file:
                st.download_button('Download Video', file, file_name=x.default_filename +
