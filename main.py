import os
import streamlit as st
import youtube_dl

def main():
    st.title("YouTube Downloader")
    
    # Get YouTube URL from user input
    url = st.text_input(label="Paste your YouTube URL")
    
    if url:
        try:
            # Download button
            if st.button("Download"):
                with st.spinner("Downloading..."):
                    # Configure options for youtube-dl
                    ydl_opts = {
                        'format': 'bestvideo+bestaudio/best',
                        'outtmpl': '%(title)s.%(ext)s',
                    }
                    
                    # Download the video
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                
                st.success('Download complete!')
            
        except Exception as e:
            st.error(e)

if __name__ == "__main__":
    main()
