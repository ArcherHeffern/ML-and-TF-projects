import tensorflow as tf

def load_model():
    return tf.keras.models.load_model('my_model')

if __name__ == '__main__':
    model = load_model()
    print(model.summary())
