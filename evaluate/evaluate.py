import os
from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator

f_model = "./results"
fn_model = "model.json"
fn_weights = "weights.hdf5"

json_string = open(os.path.join(f_model, fn_model)).read()
model = model_from_json(json_string)

model.load_weights(os.path.join(f_model,fn_weights))

model.summary()

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

test_datagen = ImageDataGenerator(rescale=1.0 / 255)

test_generator = test_datagen.flow_from_directory(
        'data/validation',
        target_size=(96, 96),
        batch_size=20,
        class_mode='binary')

print(test_generator.class_indices)

scores = model.evaluate_generator(test_generator, 500)
print('Test loss :', scores[0])
print('Test accuracy :', scores[1])
