import tensorflow_hub as hub
import tensorflow_text


def load_model():
    print('loading model')
    return hub.load("./model-directory/")
