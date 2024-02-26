import asyncio
import streamlit as st
import cv2
from PIL import Image
from aiortc.contrib.media import MediaPlayer

async def consume_audio(video_stream, audio_stream):
    while True:
        frame = await video_stream.recv()
        audio_frame = await audio_stream.recv()

        # Perform any additional processing on the frame if needed
        processed_frame = frame

        # Display the frame using st.video
        st.video(processed_frame, channels="BGR", format="jpeg")

def main():
    st.title("Camera App with Streamlit and aiortc")

    # Checkbox to start/stop the camera
    start_camera = st.checkbox("Start Camera")

    if start_camera:
        player = MediaPlayer(video_device=0, audio_device=None)
        video_stream = player.video
        audio_stream = player.audio

        # Create an asyncio task to consume the audio and video streams
        asyncio.create_task(consume_audio(video_stream, audio_stream))

        # Button to capture a photo
        if st.button("Capture Photo"):
            # Get the latest frame from the video stream
            frame, _ = video_stream.recv()

            # Save the captured frame as an image
            filename = "captured_photo.jpg"
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            image.save(filename)

            # Display the captured photo
            st.success("Photo captured successfully!")
            st.image(filename, channels="RGB", use_column_width=True)

if __name__ == "__main__":
    main()
