import streamlit as st
import pandas as pd
from PIL import Image

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home","Disease Detection", "Chatbots","About"])

#HomePage
if app_mode == "Home":
    st.header("PLANT DISEASE DETECTION SYSTEM")
    image_path = "leaves_home.jpg"
    st.image(image_path, use_container_width = True)
    st.markdown("""
    Welcome to the Plant Disease Detection System System! 🌿🔍
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Detection** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Detection** page in the sidebar to upload an image and experience the power of our Plant Disease Detection System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

#Disease Detection
if app_mode == "Disease Detection":
    def main():
        st.header("Upload Image")

        # File uploader widget for PNG and JPEG files only
        uploaded_file = st.file_uploader("Choose a PNG or JPEG file", type=["png", "jpeg", "jpg"])
        
        if uploaded_file is not None:
            # Display the file details
            st.write("Filename:", uploaded_file.name)
            st.write("File type:", uploaded_file.type)
            st.write("File size:", uploaded_file.size, "bytes")

            # If the file is an image (PNG or JPEG), display it
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_container_width=True)

    if __name__ == "__main__":
        main()

#Chatbots
if app_mode == "Chatbots":
    st.header("Chatbots")

#About Project
elif app_mode == "About":
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing 33 test images is created later for prediction purpose.
                #### Content
                1. train (70295 images)
                2. test (33 images)
                3. validation (17572 images)

                """)
