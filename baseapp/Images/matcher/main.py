from __future__ import division
import cv2
import numpy as np
from os.path import abspath, dirname as dname
from sys import argv, exit
from operator import attrgetter
import msgpack

import msgpack_numpy as mp_np
mp_np.patch()

BASE_DIR = dname(dname(abspath(__file__)))
DATA_DIR = BASE_DIR + '/data/'
EDGE_DIR = BASE_DIR + '/edges/'

class matcherClass:
	def __init__(self, name, chi2):
		self.name = name
		self.chi2_distance = chi2


def chi2_distance(histA, histB, eps = 1e-10):
	# compute the chi-squared distance
	d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])
	# return the chi-squared distance
	return d


def read_hist_data():
	f = open(DATA_DIR + 'hist_dict.mp', 'rb')
	dat = msgpack.unpackb(f.read(), object_hook=mp_np.decode)
	return dat


def match(filename):
	filename = EDGE_DIR + filename 
	sample_img = cv2.imread(filename, 0)
	test_hist = cv2.calcHist([sample_img], [0], None, [256], [0, 256])
	dat = read_hist_data()
	data, name = dat['data'], dat['name']
	matcherObj = []
	for (hist, name) in zip(data, name):
		d = chi2_distance(test_hist, hist)
		matcherObj.append(matcherClass(name, d))
	matcherObj = sorted(matcherObj, key=attrgetter('chi2_distance'))
	res = []
	for d in matcherObj[:5]:
		print "\n[", d.name, "\t", d.chi2_distance, "]"
		res.append(dict(name=d.name, chi2_distance=d.chi2_distance))

	return res


if __name__ == '__main__':
	# use python -i (interactive command)
	m = match('Air-Jordan-4-Retro-Midnight-Navy.jpg')
