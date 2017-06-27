from PIL import Image
from numpy import*
from os import listdir

# All standalone helper functions can be defined here
def loadImagesAsPixels(path):
    # return array of images
    imagesList = listdir(path)
    loadedImages = []
    pixelList = []
    for image in imagesList:
        img = Image.open(path + image)
        pixelList.append(imageToPixels(image))
        loadedImages.append(img)

    print(loadedImages)
    print(pixelList)
    return pixelList

def imageToPixels(image):
    temp=asarray(Image.open(image))
    x=temp.shape[0]
    y=temp.shape[1]*temp.shape[2]

    temp.resize((x,y)) # a 2D array
    return temp

def parseTextFile(path):
    # works for csv or txt files
    f = open(path, 'r')
    readings = []

    for t in f:
        readings.append(t)
    return readings

print(parseTextFile("/home/ricky/readings.txt"))
