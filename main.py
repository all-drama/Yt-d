import streamlit as st
import yt_dlp

def get_best_video_link(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        best_format = ydl.get_best_format(info)
        return best_format['url']

def main():
    st.title("Best Video Link Finder")

    # Get YouTube URL from user input
    url = st.text_input("Enter YouTube URL")

    if st.button("Get Best Video Link"):
        if url:
            with st.spinner("Fetching..."):
                best_link = get_best_video_link(url)
            st.success("Best Video Link:")
            st.text(best_link)

if __name__ == "__main__":
    main()
