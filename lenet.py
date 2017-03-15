import os
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping, ModelCheckpoint

nb_epoch = 150

batch_size = 30
data_augmentation = True

result_dir = 'results'
if not os.path.exists(result_dir):
    os.mkdir(result_dir)


def save_history(history, result_file):
    loss = history.history['loss']
    acc = history.history['acc']
    val_loss = history.history['val_loss']
    val_acc = history.history['val_acc']
    nb_epoch = len(acc)

    with open(result_file, 'w') as f:
        f.write("epoch\tloss\tacc\tval_loss\tval_acc\n")
        for i in range(nb_epoch):
            f.write("%d\t%f\t%f\t%f\t%f\n" % (i, loss[i], acc[i], val_loss[i], val_acc[i]))

# input image demensions
img_rows, img_cols = 96, 96

# the number of channels
img_channels = 3

input_shape = (img_rows, img_cols, img_channels)


def my_init(shape, name=None):
    return initializations.normal(shape, scale=0.1, name=name)

#here starts model

    
if __name__ == '__main__':

    model = Sequential()

    model.add(Convolution2D(32, 3, 3, border_mode='same', input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(Convolution2D(32, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Convolution2D(64, 3, 3, border_mode='same'))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.summary()

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    #save model
    model_json_str = model.to_json()
    open('results/model.json', 'w').write(model_json_str)

    model.load_weights(os.path.join("./" + result_dir + "/weights.hdf5"))

    train_datagen = ImageDataGenerator(
            rescale=1.0 / 255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1.0 / 255)

    train_generator = train_datagen.flow_from_directory(
            'data/train',
            target_size=(96, 96),
            batch_size=35,
            class_mode='binary')

    validation_generator = test_datagen.flow_from_directory(
            'data/validation',
            target_size=(96, 96),
            batch_size=50,
            class_mode='binary')

    #save weights on the way
    checkpointer = ModelCheckpoint(filepath=result_dir + "/weights.hdf5", verbose=1, save_best_only=True)
    early_stopping = EarlyStopping(monitor='val_loss', patience=10)
    
    train the model
    history = model.fit_generator(
            train_generator,
            samples_per_epoch=3500,
            nb_epoch=nb_epoch,
            validation_data=validation_generator,
            nb_val_samples=500,
            callbacks=[checkpointer, early_stopping])
    model.save_weights(os.path.join(result_dir, 'lenet.hdf5'))
    save_history(history, os.path.join(result_dir, 'history_lenet.txt'))
