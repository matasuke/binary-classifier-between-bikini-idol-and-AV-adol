import os
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping, ModelCheckpoint

nb_epoch = 100

batch_size = 100
data_augmentation = True

result_dir = 'results'
if not os.path.exists(result_dir)

