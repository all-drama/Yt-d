import streamlit as st
from pytube import YouTube
import os

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


def download_video(url):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        file_path = os.path.join("temp", f"{youtube.title}.mp4")
        video.download("temp", filename=video.title)
        return file_path
    except:
        return None


def main():
    st.title("Video URL Extractor")

    # Get YouTube URL from user input
    url = st.text_input("Enter YouTube URL")

    if st.button("Extract Video URL", key="extract"):
        if url:
            with st.spinner("Extracting..."):
                video_path = download_video(url)
            if video_path:
                st.video(video_path)
                st.markdown(
                    f'''
                    <div class="rainbow" onclick="window.open('{video_path}', '_blank');" style="cursor: pointer;">
                        <a href="{video_path}" target="_blank" style="color:#fff;text-decoration:none;">
                            Download Video
                        </a>
                    </div>
                    ''',
                    unsafe_allow_html=True
                )
            else:
                st.error("Failed to extract video URL.")


if __name__ == "__main__":
    main()
