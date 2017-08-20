import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from skimage import data, img_as_float, io
from skimage import exposure


class Equalize:
    """docstring for Equalize"""
    def __init__(self, index):
        self.image_paths = index

    def adaptive_hist(self):
        for image_path in self.image_paths:
            img = io.imread(image_path)
            img_eq = exposure.equalize_adapthist(img)
            print '[Saving ' + image_path.split('/')[-1] + ']'
            io.imsave(image_path, img_eq)