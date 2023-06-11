import streamlit as st
import yt_dlp

def get_video_formats(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])
        return formats

def main():
    st.title("Video Format and Quality Viewer")

    # Get YouTube URL from user input
    url = st.text_input("Enter YouTube URL")

    if st.button("Get Video Formats"):
        if url:
            with st.spinner("Fetching..."):
                video_formats = get_video_formats(url)
            st.success("Video Formats:")
            for format in video_formats:
                quality = format.get('format_note', 'Unknown Quality')
                st.write(f"- Quality: {quality}, URL: {format['url']}")

if __name__ == "__main__":
    main()
