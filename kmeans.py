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
CLUSTERS = 3
MEANS = []
FILE = 'face.bmp'
IMAGE = mpimg.imread(FILE)
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

def euclidean_distance(a, b):
    distance = math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2)
    return distance

if __name__ == "__main__":
    p1 = Point.get_point()
    p2 = Point.get_point()
    p3 = Point.get_point()
    MEANS.append(p1)
    MEANS.append(p2)
    MEANS.append(p3)
    print(MEANS)
    print(euclidean_distance(p1, p2))