"""ColorExtractor.
	
	Extracts a three most prominent colors from a given image.

	Excludes the most prominent color treating as background color and
	return a two color array and corresponding percentage array 
	tuple (colors, percentage) 
"""
from sklearn.cluster import KMeans
import cv2
import numpy as np


class ColorExtractor:
	"""docstring for ColorExtractor.

		None
	"""
	def __init__(self, image_file):
		image = cv2.imread(image_file)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		# reshape the image to be a list of RGB pixels rather than M * N array
		self.im = image.reshape((image.shape[0] * image.shape[1], 3))
		self.clt = KMeans(n_clusters=3)
		self.clt.fit(self.im)
		self.hist = None

	def centroid_histogram(self):
		# grab the number of different cluster and create a histogram
		# based on the number of pixels assigned to each cluster
		self.numLabels = np.arange(0, len(np.unique(self.clt.labels_)) + 1)
		(self.hist, _) = np.histogram(self.clt.labels_, bins=self.numLabels)

		# normalize the histogram such that it sums to one
		self.hist = self.hist.astype('float')
		self.hist /= self.hist.sum()

		return self.hist		

	def get_colors(self):
		if self.hist is not None:
				h = list(self.hist)
				c = list(self.clt.cluster_centers_)
				del c[h.index(max(h))]
				del h[h.index(max(h))]
				h = [(i/sum(h)) for i in h]
				if h[1] > h[0]:
					h[0], h[1] = h[1], h[0]
					c[0], c[1] = c[1], c[0]
				c = [
					c[0].astype('uint8').tolist(), 
					c[1].astype('uint8').tolist()
					]
				return (c, h)	
		else:
			raise ValueError('None Type values for [self.hist] not accepted')	
			