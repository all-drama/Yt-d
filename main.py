import streamlit as st
from pytube import YouTube

def download_youtube_video(url, output_dir):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=output_dir)
        st.success('Download successful!')
    except:
        st.error('Download failed.')

def main():
    st.header('YouTube Video Downloader')
    url = st.text_input('Enter YouTube Video URL')
    output_dir = st.text_input('Enter Output Directory', './output')

    if st.button('Download'):
        if url:
            download_youtube_video(url, output_dir)
        else:
            st.warning('Please enter a YouTube Video URL.')

if __name__ == '__main__':
    main()
