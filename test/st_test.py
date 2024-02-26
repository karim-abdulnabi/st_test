import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
from PIL import Image

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Modify this method to perform any additional processing on the frame if needed
        return frame

def main():
    st.title("Camera App with Streamlit and OpenCV")

    # Checkbox to start/stop the camera
    start_camera = st.checkbox("Start Camera")

    # Display the webcam feed using webrtc_streamer
    webrtc_ctx = webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

    if start_camera:
        if webrtc_ctx.video_transformer:
            # Get the latest frame from the webcam
            frame = webrtc_ctx.video_transformer.frame

            # Display the frame
            st.image(frame, channels="BGR", use_column_width=True)

        # Button to capture a photo
        if st.button("Capture Photo"):
            if webrtc_ctx.video_transformer:
                # Save the captured frame as an image
                filename = "captured_photo.jpg"
                image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                image.save(filename)

                # Display the captured photo
                st.success("Photo captured successfully!")
                st.image(filename, channels="RGB", use_column_width=True)
            else:
                st.warning("Start the camera before capturing a photo.")

if __name__ == "__main__":
    main()
