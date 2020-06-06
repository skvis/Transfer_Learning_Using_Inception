import config
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os
import random


def view_test_images():

    train_horses = os.listdir(os.path.join(config.TRAIN_DIR, 'horses'))
    train_humans = os.listdir(os.path.join(config.TRAIN_DIR, 'humans'))
    fig, ax = plt.subplots(2, 4, figsize=(15, 8))
    for i in range(4):
        x = random.randint(0, len(train_horses))
        ax[0, i].imshow(mpimg.imread(config.TRAIN_DIR + '/humans/' + train_humans[x]))
        ax[1, i].imshow(mpimg.imread(config.TRAIN_DIR + '/horses/' + train_horses[x]))
    plt.show()


def plot_graphs(history, string):
    plt.plot(history[string])
    plt.plot(history['val_'+string])
    plt.xlabel('Epochs')
    plt.ylabel(string)
    plt.legend([string, 'val_'+string])
    plt.show()


if __name__ == '__main__':
    view_test_images()
    # history = np.load(f'{config.MODEL_PATH}my_history.npy', allow_pickle=True).item()
    # plot_graphs(history, 'accuracy')
    # plot_graphs(history, 'loss')
