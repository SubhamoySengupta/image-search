import cv2
import numpy as np
from matplotlib import pyplot as plt
from os import walk
from sklearn.feature_selection import chi2
from matplotlib import pyplot as plt
from sys import exit
path = '/home/subhamoy/Documents/ImageProcessing/'
path2 = path + 'django_project/imagesearch/baseapp/Images/edges/'
files = []
for top, sub, f in walk(path2):
	for f_name in f:
		files.append(top + f_name)

def chi2_distance(histA, histB, eps = 1e-10):
	# compute the chi-squared distance
	d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])
	# return the chi-squared distance
	return d

im_b = cv2.imread(files[0].replace('edges', 'resized'), 0)

im = cv2.imread(files[0])
t_hist = cv2.calcHist([im], [0], None, [256], [0, 256])

hist_list = {}
h_k = []
for (index, image) in enumerate(files):
	path = image
	image = cv2.imread(image, 0)

	hist = cv2.calcHist([image], [0], None, [256], [0, 256])
	d = chi2_distance(t_hist, hist)
	
	hist_list[d] = {'index' : index, 'path':path}    
	h_k.append(d)

sorted(hist_list.keys())
i = 0
for d in hist_list:
	i += 1
	
	print d, hist_list[d]['index']
	
	i2 = cv2.imread(hist_list[d]['path'].replace('edges', 'resized'), 0)
	plt.subplot(121)
	plt.imshow(im_b, cmap='gray')
	plt.subplot(122)
	plt.imshow(i2, cmap='gray')
	plt.show()
	if i == 5:
		break
