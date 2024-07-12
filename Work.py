import os

#from skimage import imread

empty_list = []
directory = ''
categories = ['run', 'pass']


data=[]
labels = []

for c in categories:
    for file in os.listdir(os.path.join(directory, c)):
        path = os.path.join(directory, c, file)

