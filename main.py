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
                    <div style="text-align:center;padding:10px;background-color:#f1f1f1;box-shadow:0px 0px 10px 3px #f1f1f1;border-radius:10px;">
                        <p style="font-size:18px;color:#0000FF;text-decoration:none;text-shadow: 2px 2px 8px #0000FF;">
                            <a href="{video_url}" target="_blank" style="color:#0000FF;text-decoration:none;">Download Video</a>
                        </p>
                    </div>
                    ''',
                    unsafe_allow_html=True
                )
            else:
                st.error("Failed to extract video URL.")

if __name__ == "__main__":
    main()
