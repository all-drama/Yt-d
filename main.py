import streamlit as st
import yt_dlp

def get_best_video_url(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        best_format = info['formats'][0]
        return best_format['url']

def main():
    st.title("Best Quality Video URL Finder")

    # Get YouTube URL from user input
    url = st.text_input("Enter YouTube URL")

    if st.button("Get Best Quality Video URL"):
        if url:
            with st.spinner("Fetching..."):
                best_url = get_best_video_url(url)
            st.success("Best Quality Video URL:")
            st.text(best_url)

if __name__ == "__main__":
    main()
