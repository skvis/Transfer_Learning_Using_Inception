import config
import model
import data_preprocess
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, CSVLogger
import numpy as np


def train_fn():

    train_generator, valid_generator = data_preprocess.data_augmentation()

    load_model = model.load_model()

    load_model.compile(optimizer=RMSprop(lr=config.LEARNING_RATE),
                       loss='binary_crossentropy',
                       metrics=['accuracy'])

    earlystop = EarlyStopping(patience=10)
    learning_rate_reduction = ReduceLROnPlateau(monitor='val_accuracy',
                                                patience=2,
                                                verbose=1,
                                                factor=0.5,
                                                min_lr=0.00001)
    csv_logger = CSVLogger(f'{config.MODEL_PATH}training.log', separator=',', append=False)

    callbacks = [earlystop, learning_rate_reduction, csv_logger]

    history = load_model.fit(train_generator,
                             validation_data=valid_generator,
                             steps_per_epoch=len(train_generator) // config.BATCH_SIZE,
                             validation_steps=len(valid_generator) // config.BATCH_SIZE,
                             epochs=config.NUM_EPOCHS,
                             verbose=2,
                             callbacks=callbacks)

    load_model.save(f"{config.MODEL_PATH}my_model.h5")
    np.save(f'{config.MODEL_PATH}my_history.npy', history.history)


if __name__ == '__main__':
    train_fn()
