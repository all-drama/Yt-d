import streamlit as st
import pytube

def main():
    st.title("YouTube Downloader")
    
    # Get YouTube URL from user input
    url = st.text_input(label="Paste your YouTube URL")
    
    if url:
        try:
            # Create YouTube object
            yt = pytube.YouTube(url)
            
            # Get available video and audio streams
            video_streams = yt.streams.filter(file_extension="mp4").order_by('resolution')
            audio_streams = yt.streams.filter(only_audio=True)
            
            # Display video quality options
            st.subheader("Video Quality")
            for stream in video_streams:
                st.write(f"{stream.resolution} ({stream.mime_type.split('/')[1]})")
            
            # Display audio quality options
            st.subheader("Audio Quality")
            for stream in audio_streams:
                st.write(f"{stream.abr} ({stream.mime_type.split('/')[1]})")
            
            # Get user's selection
            selected_stream = st.selectbox("Select Video Quality", video_streams, format_func=lambda s: f"{s.resolution} ({s.mime_type.split('/')[1]})")
            
            if selected_stream is not None:
                # Download the selected video
                st.info(f"Downloading video: {selected_stream.default_filename}")
                selected_stream.download()
                st.success('Download complete!')
            
        except Exception as e:
            st.error(e)

if __name__ == "__main__":
    main()
