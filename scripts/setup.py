import os
import random
import shutil


#change it to be used for variable data;

source_dir = "../images"
AV_dir = "/AVimages"
bikini_dir = "/ADimages"

train_dir = "../data/train"
valid_dir = "../data/validation"

if not os.path.isdir(train_dir + "AV_idols"):
    os.makedirs(train_dir + "/AV_idols")
if not os.path.isdir(train_dir + "/bikini_idols"):
    os.makedirs(train_dir + "/bikini_idols")
if not os.path.isdir(valid_dir + "/AV_idols"):
    os.makedirs(valid_dir + "/AV_idols")
if not os.path.isdir(valid_dir + "/bikini_idols"):
    os.makedirs(valid_dir + "/bikini_idols")


AV_files = os.listdir(source_dir + AV_dir)
bikini_files = os.listdir(source_dir + bikini_dir)
random.shuffle(AV_files)
random.shuffle(bikini_files)

for i in range(3500):
    shutil.copy(source_dir + AV_dir + "/" + AV_files[i], train_dir + "/AV_idols/" + str(i) + ".jpg")
    shutil.copy(source_dir + bikini_dir + "/" + bikini_files[i], train_dir + "/bikini_idols/" + str(i) + ".jpg")

for i in range(3500,4000):
    shutil.copy(source_dir + AV_dir + "/" + AV_files[i], valid_dir + "/AV_idols/" + str(i) + ".jpg")
    shutil.copy(source_dir + bikini_dir + "/" + bikini_files[i], valid_dir + "/bikini_idols/" + str(i) + ".jpg")
