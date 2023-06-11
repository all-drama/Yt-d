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
            video_quality_options = [f"{stream.resolution} ({stream.mime_type.split('/')[1]})" for stream in video_streams]
            selected_video_quality = st.selectbox("Select Video Quality", video_quality_options)
            selected_video_stream = video_streams[video_quality_options.index(selected_video_quality)] if selected_video_quality else None
            
            # Display audio quality options
            st.subheader("Audio Quality")
            audio_quality_options = [f"{stream.abr} ({stream.mime_type.split('/')[1]})" for stream in audio_streams]
            selected_audio_quality = st.selectbox("Select Audio Quality", audio_quality_options)
            selected_audio_stream = audio_streams[audio_quality_options.index(selected_audio_quality)] if selected_audio_quality else None
            
            # Download button
            if selected_video_stream or selected_audio_stream:
                if st.button("Download"):
                    if selected_video_stream:
                        st.info(f"Downloading video: {selected_video_stream.default_filename}")
                        selected_video_stream.download()
                        st.success('Video download complete!')
                    if selected_audio_stream:
                        st.info(f"Downloading audio: {selected_audio_stream.default_filename}")
                        selected_audio_stream.download()
                        st.success('Audio download complete!')
            
        except Exception as e:
            st.error(e)

if __name__ == "__main__":
    main()
