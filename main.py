import os
import streamlit as st
import subprocess
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
                        'format': 'bestvideo+bestaudio/best',
                        'outtmpl': '%(title)s.%(ext)s',
                    }
                    
                    # Download the video using yt_dlp
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info_dict = ydl.extract_info(url, download=True)
                        video_path = ydl.prepare_filename(info_dict)
                
                # Merge audio and video using ffmpeg
                audio_path = f"{video_path}.webm"
                output_path = f"{video_path}.mp4"
                subprocess.run(['ffmpeg', '-i', video_path, '-i', audio_path, '-c', 'copy', output_path])
                
                # Remove the temporary audio and video files
                os.remove(audio_path)
                os.remove(video_path)
                
                st.success('Download complete!')
            
        except Exception as e:
            st.error(e)

if __name__ == "__main__":
    main()
