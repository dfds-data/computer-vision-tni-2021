import streamlit as st
from webcam import webcam

from src.demo import detect_age_gender

with st.sidebar:
    page = st.selectbox("Go to", ["Introduction", "Age and gender detector"], index=0)
if page == "Introduction":
    st.title("Computer Vision demo")
    st.markdown(
        """
    ### Introduction
    
    We have built a machine learning model to detect your age and gender from just an image of your face. 
    
    You can skip everything else and just try it out by selecting **"Age and gender detector"** in the dropdown to the left.
    
    If you want more details, read on. 
    
    ### Model
    We are using 2 different convolutional deep learning models.
    We find all the faces we can identify on the image with the first model. 
    For each of those faces we use the second model to find age and gender.   
    
    ### Training data
    We have used a mix of images from wikipedia and IMDB to train the models. 
    
    ### Shortcomings
    There can be a bunch of reasons the models are not performing optimally:
    
    #### Celebrities
    The bulk of the training images is the faces of celebrities. 
    This can skew the model predictions as they usually look younger than a random bunch of IT nerds [citation needed].
    They are also often PR photos, so the camera/lighting/angle/etc are much better than a laptop webcam. 
    
    
    ### Try to trick the AI
    Explore what makes the model work and especially what makes the model break. 
    We have brought some items you might try out:
    - Hat
    - Glasses
    - Fake mustache
    - Clown nose
    - Wig
    
    How does the prediction change when you try these? Are there something you can do to not be recognized at all?
    """
    )

elif page == "Age and gender detector":
    st.title("Age and gender detector")
    st.markdown(
        """
    By: D&A Data Science Chapter
    
    ### How to use this thing
    
    This tool will try to find your face and guess your age and gender. 
    
    Make sure your face is visible and that you are facing the camera. Click "Capture Frame" and wait 5-ish seconds. 
    Then you should be able to see the image you just captured, with the alogrithms guess for your age and gender.
    """
    )
    captured_image = webcam()
    if captured_image is None:
        st.write("Waiting for capture...")
    else:
        st.write("Got an image from the webcam:")
        img = detect_age_gender(captured_image)
        st.image(img)
