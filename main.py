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
            streams = yt.streams
            
            # Display quality options for video and audio
            st.subheader("Video and Audio Quality")
            quality_options = [f"{stream.resolution} ({stream.mime_type.split('/')[1]})" for stream in streams]
            selected_quality = st.selectbox("Select Quality", quality_options)
            selected_stream = streams[quality_options.index(selected_quality)] if selected_quality else None
            
            # Download button
            if selected_stream:
                if st.button("Download"):
                    st.info(f"Downloading: {selected_stream.default_filename}")
                    selected_stream.download()
                    st.success('Download complete!')
            
        except Exception as e:
            st.error(e)

if __name__ == "__main__":
    main()
