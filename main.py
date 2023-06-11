import subprocess
import streamlit as st
import os
import base64
from urllib.parse import urlparse

# CSS styles
st.markdown(
    """
    <style>
    body {
        margin-top: 150px;
        text-align: center;
    }
    .rainbow {
        background-color: #343A40;
        border-radius: 16px;
        color: #fff;
        cursor: pointer;
        padding: 12px 32px;
    }
    .rainbow:hover {
        background-image: linear-gradient(90deg, #00C0FF 0%, #FFCF00 49%, #FC4F4F 80%, #00C0FF 100%);
        animation: slide 3s linear infinite;
    }
    @keyframes slide {
        to {
            background-position: 20vw;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


def extract_links(url):
    try:
        video_output = subprocess.check_output(['yt-dlp', '--get-url', '-f', 'best', url])
        video_link = video_output.decode().strip()
        return video_link
    except subprocess.CalledProcessError:
        return None


def download_video(url, save_dir):
    try:
        subprocess.run(['yt-dlp', '-o', os.path.join(save_dir, '%(title)s.%(ext)s'), url], check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def get_binary_file_downloader_html(bin_file, file_label='File'):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
    else:
        return ""


def main():
    st.title("Video URL Extractor and Downloader")

    # Get YouTube URL from user input
    url = st.text_input("Enter YouTube URL")

    if st.button("Extract Video URL", key="extract"):
        if url:
            with st.spinner("Extracting..."):
                video_url = extract_links(url)
            if video_url:
                st.markdown(
                    f'''
                    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
                        <iframe src="{video_url}" frameborder="0" allowfullscreen
                            style="position:absolute;top:0;left:0;width:100%;height:100%;"></iframe>
                    </div>
                    ''',
                    unsafe_allow_html=True
                )
                save_dir = "downloads"  # Directory to save the video file
                os.makedirs(save_dir, exist_ok=True)  # Create the "downloads" directory if it doesn't exist
                video_name = os.path.splitext(os.path.basename(urlparse(video_url).path))[0]
                save_path = os.path.join(save_dir, f"{video_name}.mp4")  # Save the video with the original name
                if download_video(video_url, save_dir):
                    st.success("Video downloaded successfully!")
                    st.markdown(
                        get_binary_file_downloader_html(save_path, 'Download Video'),
                        unsafe_allow_html=True
                    )
                else:
                    st.error("Failed to download video.")
            else:
                st.error("Failed to extract video URL.")

    if st.button("Clear Cache"):
        # Clear downloaded video cache
        shutil.rmtree(save_dir)
       
        st.info("Cache cleared!")

    if st.button("Clear Output"):
        # Clear the displayed video and download link
        st.markdown("")
        st.markdown("")


if __name__ == "__main__":
    main()
    