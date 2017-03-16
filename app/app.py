import os
from flask import Flask, render_template, request, jsonify, Response
from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np
import base64
import cv2
from detectFace import *
import json



#model properties
f_model = "./models"
fn_model = "model.json"
fn_weighs = "weights.hdf5"

model_json = open(os.path.join(f_model, fn_model)).read()
img_row, img_col, channels = 96, 96, 3
target_size = (img_row, img_col, channels)

#for cutting images
tmp = "tmp.jpg"
cut = "cut_img.jpg"
rec = "rec.jpg"



app = Flask(__name__)


@app.route('/api', methods=['POST'])
def classifier():
    if 'file' not in request.files:
        reslut = "File doesn't exist."
        return result
    
    model = model_from_json(model_json)
    model.load_weights(os.path.join(f_model, fn_weighs))
    model.compile(loss="binary_crossentropy",
                  optimizer="adam",
                  metrics=["accuracy"])


    file = request.files['file']
    file_name = file.filename
    file.save(tmp)
    cut_img, img = detectFace(tmp)
    
    if cut_img is 0 and img is 0:
        return jsonify(results=[0])

    cv2.imwrite(rec, img)
    f2 = open(rec, 'rb')
    img2 = f2.read()
    img2 = base64.encodestring(img2)

    img1 = []
    pre1 = []
    pre2 = []

    for i in range(0,len(cut_img)):
        
        #add image to array for sending them to browser
        cv2.imwrite(cut, cut_img[i])
        f1 = open(cut, 'rb')
        img = f1.read()
        img1.append(base64.encodestring(img))
        
        #calc probability
        target = image.load_img(cut, target_size=target_size)
        x = image.img_to_array(target)
        x = np.expand_dims(x, axis=0)
        x /= 255.0
        result = model.predict(x)[0]
        
        pre1.append(str(result[0]))
        pre2.append(str(result[1]))

    os.remove(tmp)
    os.remove(cut)
    os.remove(rec)

    return jsonify(results=[img2, img1, pre1, pre2])


@app.route('/')
def index():
    title="AV女優&グラドル識別器"
    return render_template('index.html', title=title)

if __name__ == "__main__" :
    app.debug = True
    app.run()
