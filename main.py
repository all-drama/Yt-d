import random
import streamlit as st
from downloader import video, playlist, channel

# Function for some random animations
def random_celeb():
    return random.choice([st.balloons()])

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
