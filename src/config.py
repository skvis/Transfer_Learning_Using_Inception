import os

DATA_PATH = '../input/'
MODEL_PATH = '../models/'
WEIGHT_PATH = '../input/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'

TRAIN_DIR = os.path.join(DATA_PATH, 'horse-or-human')
VALID_DIR = os.path.join(DATA_PATH, 'validation-horse-or-human')
PRED_DIR = os.path.join(DATA_PATH, 'prediction_images')

IMG_WIDTH = 150
IMG_HEIGHT = 150
IMG_CHANNELS = 3
TARGET_SIZE = (IMG_WIDTH, IMG_HEIGHT)
BATCH_SIZE = 32
CLASS_MODE = 'binary'
LEARNING_RATE = 1e-4
NUM_EPOCHS = 1
