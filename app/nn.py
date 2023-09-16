import tensorflow as tf
from tensorflow.keras.models import load_model
import autokeras as ak
import numpy as np

filename = './app/saved_model'
loaded_model = load_model(filename, custom_objects=ak.CUSTOM_OBJECTS)
def predict(*args):

    predicted_y = loaded_model.predict(*args)
    return(predicted_y)