import random
import streamlit as st

# List of available animations
animations = [
    st.balloons,
    st.confetti,
    st.success("🎉 Party Time! 🥳"),
    st.success("🎆 Made By David! 🎇"),
    # Add more animations here
]

# Function for a random animation
def random_celeb():
    random_animation = random.choice(animations)
    random_animation()

# Integration of all the downloader functions
def main():
    st.title("YouTube Downloader")
    url = st.text_input(label="Paste your YouTube URL")
    if st.button("Download"):
        if url:
            try:
                with st.spinner("Loading..."):
                    if 'playlist' in url:
                        playlist(url)
                    elif 'channel' in url:
                        channel(url)
                    else:
                        video(url)
                random_celeb()
            except Exception as e:
                st.error(e)

if __name__ == "__main__":
    main()
