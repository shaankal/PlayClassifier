import os

#from skimage import imread

directory = ''
categories = ['run', 'pass']


data=[]
labels = []

for c in categories:
    for file in os.listdir(os.path.join(directory, c)):
        path = os.path.join(directory, c, file)

