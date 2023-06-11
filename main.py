import subprocess
import streamlit as st

def extract_links(url):
    try:
        video_output = subprocess.check_output(['yt-dlp', '--get-url', '-f', 'best', url])
        title_output = subprocess.check_output(['yt-dlp', '--get-title', url])
        video_link = video_output.decode().strip()
        video_title = title_output.decode().strip()
        return video_link, video_title
    except subprocess.CalledProcessError:
        return None, None

def main():
    st.title("Video URL Extractor")

    # Get YouTube URL from user input
    url = st.text_input("Enter YouTube URL")

    if st.button("Extract Video URL"):
        if url:
            with st.spinner("Extracting..."):
                video_url, video_title = extract_links(url)
            if video_url:
                st.success("Video URL:")
                st.text(video_url)
                st.success("Video Title:")
                st.text(video_title)
            else:
                st.error("Failed to extract video URL.")

if __name__ == "__main__":
    main()
