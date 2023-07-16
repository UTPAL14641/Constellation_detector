import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
from tensorflow import keras


model = keras.models.load_model('model.h5')
# Load the saved model


# Define the class labels
class_labels = ['Aquarius', 'Aries', 'Cancer', 'Capricornus', 'Gemini', 'Leo', 'Libra', 'Pisces', 'Sagittarius', 'Scorpius', 'Taurus','Virgo']

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((300, 300))  # Resize the image to match the input size of the model
    image = np.array(image)  # Convert PIL image to NumPy array
    image = image / 255.0  # Normalize pixel values to the range of 0-1
    image = np.expand_dims(image, axis=0)  # Add an extra dimension to match the model's input shape
    return image

# Function to make predictions
def predict(image):
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)
    predicted_class_index = np.argmax(predictions[0])
    predicted_label = class_labels[predicted_class_index]
    return predicted_label

# Streamlit web app code
st.title('Constellation Recognition')
uploaded_image = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Predict'):
        predicted_label = predict(image)
        st.write('Predicted Label:', predicted_label)
