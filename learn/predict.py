import sys
import os
from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np

if len(sys.argv) != 2:
    print("UAGE: python predict.py [file_name]")
    sys.exit(1)

file_name = sys.argv[1]

if not os.path.isfile(file_name):
    print("File doesnt't exist")
    sys.exit(1)

print("input file: ", file_name)


f_model = "./results"
fn_model = "model.json"
fn_weights = "weights.hdf5"

AV_idol = 0
bikini_idol = 1

json_string = open(os.path.join(f_model, fn_model)).read()
model = model_from_json(json_string)

model.load_weights(os.path.join(f_model, fn_weights))

img_row, img_col = 96, 96
channels = 3

target_size = (img_row, img_col, channels)

model.compile(loss="binary_crossentropy",
              optimizer="adam",
              metrics=['accuracy'])

#model.summary()

img = image.load_img(file_name, target_size=target_size)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

x /= 255.0

pre = model.predict(x)[0]

result = "グラドル" if pre >= 0.5 else "AV女優"

print(pre)
print("お前の顔は" +  result)
