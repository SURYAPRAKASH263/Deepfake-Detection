import tensorflow as tf
from tensorflow.keras.models import load_model

def custom_lstm(**kwargs):
    kwargs.pop("time_major", None)  # Remove 'time_major' if present
    return tf.keras.layers.LSTM(**kwargs)

def load_custom_model(model_path):
    return load_model(model_path, custom_objects={"LSTM": custom_lstm})
