#Organizes the image folder to groups by species

import csv
import os
import shutil

file = open('train.csv')

csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

images = []
species = []

for image in csvreader:
    images.append(image[0])
    species.append(image[1])

for i in range (3):
    print (images[i])

mainPath = "test_images_100"

list = os.listdir(mainPath)
    
for file in list:
    path = os.path.join(mainPath, species[images.index(file)])
    if (species[images.index(file)] not in os.listdir(mainPath)):        
        os.makedirs(path)
    
    currPath = os.path.join(mainPath, file)
    shutil.move(currPath, path)
    