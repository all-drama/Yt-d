import subprocess
import streamlit as st

def extract_links(url):
    try:
        video_output = subprocess.check_output(['yt-dlp', '--get-url', '-f', 'best', url])
        video_link = video_output.decode().strip()
        return video_link
    except subprocess.CalledProcessError:
        return None

def main():
    st.title("Video URL Extractor")

    # Get YouTube URL from user input
    url = st.text_input("Enter YouTube URL")

    if st.button("Extract Video URL"):
        if url:
            with st.spinner("Extracting..."):
                video_url = extract_links(url)
            if video_url:
                st.video(video_url)
                st.markdown(f'<a href="{video_url}" target="_blank">Download Video</a>', unsafe_allow_html=True)
            else:
                st.error("Failed to extract video URL.")

if __name__ == "__main__":
    main()
