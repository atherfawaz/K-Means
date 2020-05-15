import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import time
import copy
import cv2
import random
from PIL import Image

#GLOBALS    
FILE = 'face.bmp'
IMAGE = mpimg.imread(FILE)
plt.imshow(IMAGE)

if __name__ == "__main__":
    print('Start')