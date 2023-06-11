import streamlit as st
import os
from pytube import YouTube
import requests
import base64

def download_youtube_video(url, output_dir):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        filename = stream.default_filename
        output_path = os.path.join(output_dir, filename)
        stream.download(output_path=output_path)
        st.success('Download successful!')
        return output_path
    except:
        st.error('Download failed.')
        return None

def get_download_link(file_path):
    with open(file_path, 'rb') as file:
        encoded_file = base64.b64encode(file.read()).decode()
        download_link = f'<a href="data:file/mp4;base64,{encoded_file}" download>Download Video</a>'
        return download_link

def main():
    st.header('YouTube Video Downloader')
    url = st.text_input('Enter YouTube Video URL')
    output_dir = st.text_input('Enter Output Directory', './output')

    if st.button('Download'):
        if url:
            file_path = download_youtube_video(url, output_dir)
            if file_path:
                download_link = get_download_link(file_path)
                st.markdown(download_link, unsafe_allow_html=True)
        else:
            st.warning('Please enter a YouTube Video URL.')

if __name__ == '__main__':
    main()
