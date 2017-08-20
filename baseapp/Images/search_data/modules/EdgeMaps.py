"""CannyEdge selector.

	Returns canny edge numpy array for the selected image
"""
import numpy as np
from scipy import ndimage as ndi
from skimage import feature
import cv2
from matplotlib import pyplot as plt 


class EdgeMaps(object):
	"""docstring for EdgeMaps.
		
		None
	"""
	def __init__(self, image_file, sigma):
		self.im = cv2.imread(image_file, 0)	
		self.edges = feature.canny(self.im, sigma=sigma)	

	def as_array(self):
		return self.edges.astype('uint8').tolist()

	def save_2d_image(self, path):
		plt.imshow(self.edges, cmap='gray')
		plt.xticks([]), plt.yticks([])
		plt.savefig(path)
		# plt.show()

