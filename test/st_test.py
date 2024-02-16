import streamlit as st
import cv2
import numpy as np
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
def main():
    st.title("Camera App with OpenCV and Streamlit")

    # Checkbox to start/stop the camera
    start_camera = st.checkbox("Start Camera")

    # Display live camera feed when the checkbox is selected
    if start_camera:
        st.sidebar.header("Camera Settings")
        camera = cv2.VideoCapture(0)  # 0 corresponds to the default camera

        # Adjust camera settings through sidebar sliders
        brightness = st.sidebar.slider("Brightness", 0, 100, 50)
        camera.set(10, brightness)

        # Read and display camera frames
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        st.image(frame, channels="RGB", use_column_width=True)

    # Button to capture a photo
    if st.button("Capture Photo"):
        if start_camera:
            # Capture a frame when the button is clicked
            _, frame = camera.read()

            # Save the captured frame as an image
            filename = "captured_photo.jpg"
            cv2.imwrite(filename, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Display the captured photo
            st.success("Photo captured successfully!")
            st.image(filename, channels="RGB", use_column_width=True)
        else:
            st.warning("Start the camera before capturing a photo.")

if __name__ == "__main__":
    main()
