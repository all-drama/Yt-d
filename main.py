import os
import requests
import streamlit as st

DOWNLOADS_DIR = "downloads"

def download_video(url):
    filename = url.split("/")[-1]
    filepath = os.path.join(DOWNLOADS_DIR, filename)
    if os.path.isfile(filepath):
        return filepath  # File already exists, return the filepath
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, "wb") as file:
            file.write(response.content)
        return filepath  # File downloaded successfully
    else:
        return None  # Failed to download the file

def main():
    st.title("Video Downloader")

    youtube_url = st.text_input("Enter YouTube URL")
    if st.button("Download Video"):
        if youtube_url:
            video_url = extract_video_url(youtube_url)
            if video_url:
                file_path = download_video(video_url)
                if file_path:
                    st.success("Video downloaded successfully!")
                    st.download_button(
                        label="Download",
                        data=open(file_path, "rb").read(),
                        file_name=os.path.basename(file_path),
                        mime="video/mp4"
                    )
                else:
                    st.error("Failed to download the video.")
            else:
                st.error("Failed to extract video URL.")
        else:
            st.warning("Please enter a valid YouTube URL.")

if __name__ == "__main__":
    main()
