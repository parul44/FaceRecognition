import os

def templateDir():
    subdir=[]
    for x in os.listdir('templates'):
        subdir.append(float(x))

    return subdir