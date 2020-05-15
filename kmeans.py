import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import time
import math
import copy
import cv2
import random
from PIL import Image

#GLOBALS   
MAX_ITERS = 100 
CLUSTERS = 3
MEANS = []
FILE = 'face.bmp'
IMAGE = mpimg.imread(FILE) #dims = 220x200x3
UPDATED_MEANS = [[0 for x in range(CLUSTERS)] for x in range(0)]
BOOKKEEPING = [[0 for x in range(CLUSTERS)] for x in range(int(IMAGE.size/3))]
plt.imshow(IMAGE)
random.seed(time.perf_counter())

class Point:
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    z = random.randint(0, 255)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        pt = '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
        return pt
    
    def __str__(self):
        pt = '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
        return pt 

    def get_point():
        return Point(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def euclidean_distance(pixel, point):
    distance = math.sqrt((pixel[0] - point.x)**2 + (pixel[1] - point.y)**2 + (pixel[2] - point.z)**2)
    return distance

if __name__ == "__main__":
    '''p1 = Point.get_point()
    p2 = Point.get_point()
    p3 = Point.get_point()'''
    img_flattened = np.reshape(IMAGE, (44000,3))
    for i in range(0,CLUSTERS):
        MEANS.append(Point.get_point())
    
change = True 
iters = 0
while (change is not False and iters!=MAX_ITERS):
    print(MEANS)
    pixelIndex = 0
    for i in IMAGE:
        for pixel in i:
            counter = 0
            minimum = 1000000
            for mean in MEANS:
                distance = euclidean_distance(pixel, mean)
                if (distance < minimum):
                    minimum = distance
                    minIndex = counter
                counter+=1
            BOOKKEEPING[pixelIndex][minIndex] = 1
            pixelIndex+=1
    
    #Updating means
    bookkeeping_tp = np.transpose(BOOKKEEPING)
    for i in range(0,CLUSTERS):
        quotient = np.count_nonzero(bookkeeping_tp[i] == 1)
        print("This is the ", i+1, " mean count: ", quotient)
        if (quotient!=0):
            TEMP = np.dot(bookkeeping_tp[i],img_flattened)/quotient
            MEANS[i].x = TEMP[0]
            MEANS[i].y = TEMP[1]
            MEANS[i].z = TEMP[2]
    BOOKKEEPING = [[0 for x in range(CLUSTERS)] for x in range(int(IMAGE.size/3))]
    iters+=1

    