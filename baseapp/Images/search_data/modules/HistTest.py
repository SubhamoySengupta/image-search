import cv2


class HistTest:
	def __init__(self, filename):
		self.im = cv2.imread(filename, 0)
		self.hist = cv2.calcHist([self.im], [0], None, [256], [0, 256])
