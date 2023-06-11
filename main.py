import os
import streamlit as st
import yt_dlp

def main():
    st.title("YouTube Downloader")

    # Get YouTube URL from user input
    url = st.text_input(label="Paste your YouTube URL")

    if url:
        try:
            # Download button
            if st.button("Download"):
                with st.spinner("Downloading..."):
                    # Configure options for yt_dlp
                    ydl_opts = {
                        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                        'outtmpl': '%(title)s.%(ext)s',
                    }

                    # Download the video using yt_dlp
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])

                st.success('Download complete!')

        except Exception as e:
            st.error(e)

if __name__ == "__main__":
    main()
