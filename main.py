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

    # Create a dictionary to store resolution and corresponding streams
    resolution_dict = {}
    for stream in streams:
        resolution = f"{stream.resolution} ({stream.mime_type.split('/')[1]})"
        resolution_dict[resolution] = stream

    # Get the available resolutions
    resolutions = list(resolution_dict.keys())

    # Display resolution options
    resolution = st.selectbox("Select Video Resolution", resolutions)

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

# Integration of all the downloader functions
def main():
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
                random_celeb()
            except Exception as e:
                st.error(e)

if __name__ == "__main__":
    main()
