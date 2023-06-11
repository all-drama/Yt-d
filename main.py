import os
import streamlit as st
from pytube import YouTube
from moviepy.editor import *

def main():
    st.title("YouTube Downloader")
    
  
    url = st.text_input(label="Paste your YouTube URL")
    
    if url:
        try:
            
            if st.button("Download"):
                with st.spinner("Downloading..."):
                  
                    yt = YouTube(url)
                    
                  
                    video_stream = yt.streams.get_highest_resolution()
                    audio_stream = yt.streams.get_audio_only()
                    
                 
                    video_path = video_stream.download()
                    audio_path = audio_stream.download()
                    
                  
                    video = VideoFileClip(video_path)
                    audio = AudioFileClip(audio_path)
                    final_video = video.set_audio(audio)
                    
                   
                    output_path = f"{yt.title}.mp4"
                    final_video.write_videofile(output_path, codec="libx264")
                    
                   
                    os.remove(video_path)
                    os.remove(audio_path)
                
                st.success('Download complete!')
            
        except Exception as e:
            st.error(e)

if __name__ == "__main__":
    main()
