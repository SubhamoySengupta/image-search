import modules
import os
from os.path import dirname as dname
from sys import argv, exit

BASE_DIR = dname(dname(os.path.abspath(__file__)))
ORIGINAL_DIR = BASE_DIR + '/original/'
EDGE_DIR = BASE_DIR + '/edges/'
RESIZED_DIR = BASE_DIR + '/resized/'
DATA_DIR = BASE_DIR + '/data/'


def read_index():
	index = modules.utils.check()
	return index

def color_d(fname):
	fname = RESIZED_DIR + fname
	return modules.utils.color_d(fname)

def color():
	index = read_index()
	index = [RESIZED_DIR + i.split('/')[-1] for i in index]
	color_gen = modules.utils.color_fn(index)
	COLOR_DICT = modules.utils.cdict()
	COLOR_DICT.new(color_gen, index)
	COLOR_DICT.save()


def canny():
	index = read_index()
	index = [RESIZED_DIR + i.split('/')[-1] for i in index]
	modules.utils.edge_fn(index)
	

def hist():
	index = read_index()
	index = [EDGE_DIR + i.split('/')[-1] for i in index]
	h_gen = modules.utils.hist_fn(index)
	H_DICT = modules.utils.hdict()
	H_DICT.new(h_gen, index)
	H_DICT.save()


def help():
	print '''
	============================================
	List of Arguments available:
	1. read_index - returns list of original image from 'original/' directory
	2. color      - Update/save color data in a file in 'data/' directory
	3. canny      - Extract edges from all images and save it as a 2d image in 'edge/' directory 
	4. hist       - Update/save histogram data of canny edge images in a file in 'data/' directory
	5. help       - show this :)
	'''

if __name__ == '__main__':
	if len(argv) > 1:
		try:
			eval(argv[1] + '()')
		except:
			raise TypeError('No such function exists')
	else:
		help()
		raise Exception('No arguments passed! Exiting code :)')
		exit(0)