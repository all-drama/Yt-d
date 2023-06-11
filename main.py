import subprocess
import streamlit as st

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

def main():
    st.title("Video URL Extractor")

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
                st.markdown(
                    f'''
                    <div class="rainbow">
                        <a href="{video_url}" target="_blank" style="color:#fff;text-decoration:none;">
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
