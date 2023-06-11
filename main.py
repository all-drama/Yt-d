import random
import streamlit as st
import pytube

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
                        st.info(f"Downloading: {selected_stream.default_filename}")
                        selected_stream.download()
                        st.success('Download complete!')
                
                random_celeb()
                
            except Exception as e:
                st.error(e)

if __name__ == "__main__":
    main()
