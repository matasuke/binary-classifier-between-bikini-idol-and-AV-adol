import matplotlib.pyplot as plt
import numpy as np

def depictGraph(file):
    
    epoch = []
    acc = []
    val_acc = []
    loss = []
    val_loss = []

    with open(file, 'r') as f:
        datas = f.readlines()[1:]
        for line in datas:
            l = line.split('\t')
            epoch.append(float(l[0]))
            loss.append(float(l[1]))
            acc.append(float(l[2]))
            val_loss.append(float(l[3]))
            val_acc.append(float(l[4][:-1]))
    
    fig = plt.figure()
