import tensorflow as tf

def create_model():
    model = tf.keras.Sequential([
        # ...existing code...
        tf.keras.layers.LSTM(units=128),  # Removed 'time_major' argument
        # ...existing code...
    ])
    # ...existing code...
    return model
