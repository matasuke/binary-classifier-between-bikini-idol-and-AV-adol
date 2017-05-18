import numpy as np
import os
from os import path
import cv2
import sys

class detectFaces():
    
    def __init__(self):
        self.cascade_dir = path.normpath(path.join(cv2.__file__, '..', '..', '..', '..', 'pkgs', 'opencv3-3.1.0-py35_0', 'share', 'OpenCV', 'haarcascades'))
        #self._cascade_f = "/Users/Matasuke/.pyenv/versions/anaconda3-4.0.0/pkgs/opencv3-3.1.0-py35_0/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
        self._cascade_f = cv2.CascadeClassifier(path.join(self._cascade_dir, 'haarcascade_frontalface_alt.xml')
        self._cascade_e = cv2.CascadeClassifier(path.join(self._cascade_dir, 'haarcascade_eye.xml')
    
    def _addRectangle(self, color = (255, 0, 0), thickness = 3):
        self.resultImg = self.img
        for (x, y, w, h) in self._faces:
            cv2.rectangle(self.resultImg, (x, y), (x+w, y+h), color, thickness)
         
    def showImg(self):
        cv2.imshow('img',self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def showGrayScale(self):
        cv2.imshow('grayScale', self.imgGray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def showResultImg(self):
        self._addRectangle()
        cv2.imshow('ResultImage', self.resultImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def showFaces(self):
        for i in range(0, self.numFaces):
            cv2.imshow('cut_image', self.detectedFaces[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def saveGrayScale(self, name=None):
        if name is None:
            name = self.name + '_grayScale.' + self.extension
        cv2.imwrite(name, self.imgGray)

    def saveResultImg(self, name=None):
        self._addRectangle()
        if name is None:
            name = self.name + '_ResultImg.' + self.extension
        cv2.imwrite(name, self.resultImg)

    def saveFaces(self, name=None):
        if name is None:
            name = [self.name + '_face_' + str(num) + '.' + self.extension for num in range(1, self.numFaces + 1)]
        
        if len(name) is not self.numFaces:
            print('input ', self.numFaces, 'names')
        else: 
            for i in range(0, self.numFaces):
                cv2.imwrite(name[i], self.detectedFaces[i])

    def detectFaces(self, source, scaleFactor=1.1, minNeighbors=1, minSize=(50, 50)):
        self.processGrayScale(source) 
        self._faces = self._cascade_f.detectMultiScale(self.imgGray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)
        self.numFaces = len(self._faces)
        
        self.detectedFaces = []
        if len(self._faces) > 0:
            for(x, y, w, h) in self._faces:
                self.detectedFaces.append(self.img[y:y+h, x:x+w])

    def _processFile(self, source):
        self.name = source.split('.')[0]
        self.extension = source.split('.')[1]
        self.img = cv2.imread(source)

    def processGrayScale(self, source):
        self._processFile(source)
        self.imgGray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def rotateFrame(self, source):
        self.processGrayScale(source)
        rows, cols, channels = self.img.shape
        hypot = int(math.hypot(rows, cols)) #create rectangle size of hypot
        frame = np.zeros((hypot, hypoy), np.uint8)
        frame[(hypot - rows)*0.5 : (hypot + rows)*0.5, (hypot - cols)*0.5 : (hypot + cols)*0.5] = self.imgGray

        for deg in range(-30, 30, 5):
            M = cv2.getRotationMatrix2D((hypot * 0.5, hypot * 0.5), -deg, 1.0)
            rotated = cv2.wrapAffine(frame, M, (hypot, hypot))
            faces = self._cascade_f.detectMultiScale(rotated, scaleFactor=1.1, minNeighbors=1, minSize=(50, 50))
            numFaces = len(faces)
            for (x, y, w, h) in faces:
                

class processDir(detectFaces):
    def __init__(self, dir):
        super(processDir, self).__init__()
        self.dir = dir + '/'
        self.files = os.listdir(self.dir)[1:]

    def saveGrayScales(self, dir=os.getcwd() + '/grayScales'):
        if not os.path.isdir(dir):
            os.mkdir(dir)
        
        for file in self.files:
            super(processDir, self).processGrayScale(self.dir + file)
            name = dir + '/' + file.split('.')[0] + '_grayScale.' + file.split('.')[1]
            super(processDir, self).saveGrayScale(name)

    def saveResultImgs(self, dir=os.getcwd() + '/ResutImg'):
        if not os.path.isdir(dir):
            os.mkdir(dir)

        for file in self.files:
            super(processDir, self).detectFaces(self.dir + file)
            name = dir + '/' + file.split('.')[0] + '_resultImg.' + file.split('.')[1]
            super(processDir, self).saveResultImg(name)

    def saveAllFaces(self, dir=os.getcwd() + '/Faces'):
        if not os.path.isdir(dir):
            os.mkdir(dir)

        for file in self.files:
            super(processDir, self).detectFaces(self.dir + file)
            name = [dir + '/' +  file.split('.')[0] + '_face_' + str(num) + '.' + file.split('.')[1] for num in range(1, self.numFaces + 1)]
            super(processDir, self).saveFaces(name)


if __name__ == "__main__":
    args = sys.argv
    argc = len(args)

    if argc != 2:
        print("USAGE: python getFaces.py [dir name]")
        sys.exit(1)
 
    
    data = processDir(args[1])
    data.saveAllFaces()

