import streamlit as st
import cv2
from PIL import Image

def main():
    st.title("Camera App with Streamlit")

    # Create a button to start the camera
    start_camera = st.button("Start Camera")

    if start_camera:
        # Open the camera
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            st.error("Error: Could not open the camera.")
            st.stop()

        # Create a button to capture a photo
        capture_button = st.button("Capture Photo")

        # Display the video feed
        while start_camera:
            ret, frame = cap.read()

            if not ret:
                st.error("Error: Could not read a frame from the camera.")
                break

            # Display the frame using st.image
            st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB", use_column_width=True)

            # Check if the capture button is clicked
            if capture_button:
                # Save the captured frame as an image
                filename = "captured_photo.jpg"
                image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                image.save(filename)

                # Display the captured photo
                st.success("Photo captured successfully!")
                st.image(filename, channels="RGB", use_column_width=True)

        # Release the camera when the app stops
        cap.release()

if __name__ == "__main__":
    main()
