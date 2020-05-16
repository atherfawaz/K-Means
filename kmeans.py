import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import time
import math
import copy
import cv2
import random
from PIL import Image

# GLOBALS
MAX_ITERS = 20
MAX_CLUSTERS = 10
MEANS = []
PREV_MEANS = []
FILE = 'face.bmp'
IMAGE = mpimg.imread(FILE)  # dims = 220x200x3
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

    def __cmp__(self,other):
        if self.x < other.x and self.y < other.y and self.z < other.z:
            return -1
        elif self.x > other.x and self.y > other.y and self.z > other.z:
            return 1
        else:return 0


def euclidean_distance(pixel, point):
    distance = math.sqrt((pixel[0] - point.x)**2 +
                         (pixel[1] - point.y)**2 + (pixel[2] - point.z)**2)
    return distance


if __name__ == "__main__":
    for CLUSTERS in range(6,MAX_CLUSTERS+1):
        MEANS = []
        PREV_MEANS = []
        UPDATED_MEANS = [[0 for x in range(CLUSTERS)] for x in range(0)]
        BOOKKEEPING = [[0 for x in range(CLUSTERS)] for x in range(int(IMAGE.size/3))]
        print ("Number of clusters: ", CLUSTERS)
        img_flattened = np.reshape(IMAGE, (44000, 3))
        for i in range(0, CLUSTERS):
            MEANS.append(Point.get_point())
        for i in range(0, CLUSTERS):
            PREV_MEANS.append(Point.get_point())
        change = True
        iters = 0

        while (change is True and iters != MAX_ITERS):
            print(MEANS)
            BOOKKEEPING = [[0 for x in range(CLUSTERS)] for x in range(int(IMAGE.size/3))]
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
                        counter += 1
                    if (minIndex < 0 or minIndex >= CLUSTERS):
                        dummy = 1
                    BOOKKEEPING[pixelIndex][minIndex] = 1
                    pixelIndex += 1

            # Updating means
            bookkeeping_tp = np.transpose(BOOKKEEPING)
            for i in range(0, CLUSTERS):
                divisor = np.count_nonzero(bookkeeping_tp[i] == 1)
                print("This is the ", i+1, " mean count: ", divisor)
                if (divisor != 0):
                    TEMP = np.dot(bookkeeping_tp[i], img_flattened)/divisor
                    MEANS[i].x = int(TEMP[0])
                    MEANS[i].y = int(TEMP[1])
                    MEANS[i].z = int(TEMP[2])
                else:
                    MEANS[i] = Point.get_point()

            change = False
            for i in range(0,len(MEANS)):
                if MEANS[i].x != PREV_MEANS[i].x or MEANS[i].y != PREV_MEANS[i].y or MEANS[i].z != PREV_MEANS[i].z:
                    change = True
                else:
                    dummy = 1
            PREV_MEANS = copy.deepcopy(MEANS)
            iters += 1

        img_flattened = np.array(img_flattened)

        for x in range(0, 44000):
            for y in range(0, CLUSTERS):
                if (BOOKKEEPING[x][y] is 1):
                    img_flattened[x][0] = MEANS[y].x
                    img_flattened[x][1] = MEANS[y].y
                    img_flattened[x][2] = MEANS[y].z
        print(MEANS)
        print("--------------------")
        img_flattened = np.reshape(img_flattened, (220, 200, 3))
        imgplot = plt.imshow(img_flattened)
        file_name = "Reduced" + str(CLUSTERS) + ".bmp"
        plt.imsave(file_name, img_flattened.astype(np.uint8))