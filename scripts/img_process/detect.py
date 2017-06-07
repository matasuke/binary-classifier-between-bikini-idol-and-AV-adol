import sys
import cv2
import numpy as np
import math
import imagehash
from os import path

cascades_dir = path.normpath(path.join(cv2.__file__, '..', '..', '..', '..', 'share', 'OpenCV', 'haarcascades'))
cascade_f = cv2.CascadeClassifier(path.join(cascades_dir, 'haarcascade_frontalface_alt2.xml'))
cascade_e = cv2.CascadeClassifier(path.join(cascades_dir, 'haarcascade_eye.xml'))

def eyeDistance(eyes):
    dist = 0
    if len(eyes) == 2:
        dist = eyes[0][0] - eyes[1][0]
    return dist

def detect(img):

    results = []
    shape = img.shape
    rows, cols, channels = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hypot = int(math.ceil(math.hypot(rows, cols)))
    rect = np.zeros((hypot, hypot), np.uint8)
    rect[int((hypot - rows) * 0.5):int((hypot + rows) * 0.5), int((hypot - cols) * 0.5):int((hypot + cols) * 0.5)] = gray
    rect_origin = np.zeros((hypot, hypot, 3), np.uint8)
    rect_origin[int((hypot - rows) * 0.5):int((hypot + rows) * 0.5), int((hypot - cols) * 0.5):int((hypot + cols) * 0.5)] = img
    
    for deg in range(-48, 49, 6):
        Mat = cv2.getRotationMatrix2D((hypot * 0.5, hypot * 0.5), deg, 1.0)
        rotated = cv2.warpAffine(rect, Mat, (hypot, hypot))
        faces = cascade_f.detectMultiScale(rotated, 1.08, minNeighbors=1, minSize=(50, 50))
        
        print('deg:{0} faces:{1}'.format(deg, len(faces)))

        for (x, y, w, h) in faces:
            roi = rotated[y : y + h, x: x + w]
            eyes = cascade_e.detectMultiScale(roi, 1.05)
            if eyeDistance(eyes) > w / 4:
                original = cv2.warpAffine(rect_origin, Mat, (hypot, hypot))
                cut = original[y : y + h, x: x + w]
                results.append(cut)

    return results
