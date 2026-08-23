import tensorflow as tf
import numpy as np
import streamlit as st


@st.cache_resource
def load_model():
    return tf.keras.models.load_model("trained_model.h5")


def model_prediction(test_image):

    model = load_model()
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    predictions = model.predict(input_arr)
    result_index = np.argmax(predictions[0])
    confidence = np.max(predictions[0])

    return result_index, confidence