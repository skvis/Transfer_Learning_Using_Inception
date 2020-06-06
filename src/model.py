import config
from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.applications.inception_v3 import InceptionV3


def load_model():

    pre_trained_model = InceptionV3(include_top=False,
                                    weights=None,
                                    input_shape=(config.IMG_WIDTH, config.IMG_HEIGHT, config.IMG_CHANNELS))

    pre_trained_model.load_weights(config.WEIGHT_PATH)

    pre_trained_model.trainable = False

    # print(pre_trained_model.summary())

    x = layers.Flatten()(pre_trained_model.output)
    x = layers.Dense(512, activation='relu')(x)
    x = layers.Dropout(0.2)(x)
    x = layers.Dense(1, activation='sigmoid')(x)
    model = Model(pre_trained_model.input, x)

    # print(model.summary())

    return model


if __name__ == '__main__':
    load_model()
