import os
from os.path import dirname as dname
import msgpack
from sys import argv, exit
from ColorExtractor import ColorExtractor
from EdgeMaps import EdgeMaps
from HistTest import HistTest
from time import time

import msgpack_numpy as mp_np
mp_np.patch()

DATA_DIR = dname(dname(dname(os.path.abspath(__file__)))) + '/data/'


def check():
	if os.path.isfile(DATA_DIR + 'index.mp'):
		f = open(DATA_DIR + 'index.mp', 'rb')
		data = f.read()
		f.close()
		data = msgpack.unpackb(data)
		return data
	else:
		raise Exception('Couldnot find index.mp')


def color_d(index):
	c = ColorExtractor(index)
	c.centroid_histogram()
	color = c.get_colors()
	return color


def color_fn(index):
	for count, image_file in enumerate(index):
		c = ColorExtractor(image_file)
		c.centroid_histogram()
		color = c.get_colors()
		yield color
		

def edge_fn(index):
	for count, image_file in enumerate(index):
		e = EdgeMaps(image_file, sigma=1)
		edge_array = e.as_array()
		name = image_file[image_file.rfind('/'):]
		path = image_file[:image_file.rfind('/')]
		path = path[:path.rfind('/')]
		path += '/edges' + name
		e.save_2d_image(path)
		# break
		print '[Saving Image ==> ', path.split('/')[-1] ,']'


def hist_fn(index):
	for image_file in index:
		h = HistTest(image_file)
		yield h.hist


class hdict:
	def __init__(self):
		self.dat = {}
		self.dat['data'] = [] 
		self.dat['name'] = []

	def new(self, h_gen, index):
		for im, hist in zip(index, h_gen):
			self.update(im.split('/')[-1], hist)
			print '[Current Image ==> ', im.split('/')[-1], ']'

	def update(self, im, h):
		self.dat['data'].append(h)
		self.dat['name'].append(im)		

	def save(self):
		f = open(DATA_DIR + 'hist_dict.mp', 'wb')
		mp = msgpack.packb(self.dat, default=mp_np.encode)
		f.write(mp)
		f.close()


class cdict:
	def __init__(self):
		self.dat = {}
		self.dat['data'] = []
		self.dat['c_list'] = {}
		self.dat['c_list']['primary'] = []
		self.dat['c_list']['secondary'] = []
		self.dat['pc_list'] = []

	def new(self, cgen, index):
		print '[Extracting Colors.. ]'
		t1 = time()
		for  count, c_tuple in enumerate(zip(cgen, index)):
			print '[', count, ' ==> ', c_tuple[1].split('/')[-1], ']'
			self.update(c_tuple[1].split('/')[-1], c_tuple[0], count + 1)	
		print '[Done]'
		print '[Time taken ==> ', time() - t1, ' secs]'

	def update(self, f, r, i):
		s= {}
		s['id'] = i
		s['name'] = f
		s['colors'] = {}
		s['colors']['1'] = {}
		s['colors']['2'] = {}

		s['colors']['1']['rgb'] = r[0][0]
		s['colors']['1']['percent'] = r[1][0]
		s['colors']['2']['rgb'] = r[0][1]
		s['colors']['2']['percent'] = r[1][1]
		self.dat['data'].append(s)
		self.dat['c_list']['primary'].append(r[0][0])
		self.dat['c_list']['secondary'].append(r[0][1])
		self.dat['pc_list'].append((r[1][0], r[1][1]))

	def save(self):
		f = open(DATA_DIR + 'color_dict.mp', 'wb')
		mp = msgpack.packb(self.dat, default=mp_np.encode)
		f.write(mp)
		f.close()
