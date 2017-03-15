# -*- encode: utf-8 -*-

import cv2
import numpy as np
import sys


def detectFace(pic):
    
    cascadePath = "/Users/Matasuke/.pyenv/versions/anaconda3-4.0.0/pkgs/opencv3-3.1.0-py35_0/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
    
    img = cv2.imread(pic)
    img2 = cv2.imread(pic)

    #get cascade
    cascade = cv2.CascadeClassifier(cascadePath)
   
    # rectangle color
    color = (255, 0, 0)
     
    imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    #cascade
    faces = cascade.detectMultiScale(imageGray, scaleFactor=1.1, minNeighbors=1, minSize=(50, 50))

    # show rectangle on pic
    cut_img = []
    if len(faces) > 0:   
        #for rect in facerect:
        for (x, y, w, h) in faces:
            cut_img.append(img[y:y+h,x:x+w])
            cv2.rectangle(img2, (x, y),(x+w, y+h), color, thickness=3)
    
        return cut_img, img2
    
    else:
        return (0, 0)
    
    

if __name__ == '__main__':
    
    pic = sys.argv[1]
    cut_img, img = detectFace(pic)
    
    #show the frame 
    cv2.imshow("image", cut_img[0])
    cv2.imshow("image2", img)
    cv2.waitKey(0)
