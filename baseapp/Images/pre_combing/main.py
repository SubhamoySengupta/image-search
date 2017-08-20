import comb
import os
from sys import argv, exit


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGINAL_DIR = BASE_DIR + '/original/'
EDGE_DIR = BASE_DIR + '/edges/'
RESIZED_DIR = BASE_DIR + '/resized/'
THUMB_DIR = BASE_DIR + '/thumbnails/'


def update_index():
	return comb.utils.check(ORIGINAL_DIR)


def equalize():
	index, new = update_index()
	e = comb.Equalize(index)
	e.adaptive_hist()


def thumbs():
	index, new = update_index()
	comb.create_thumbnails.save_thumbnails(index, THUMB_DIR)


def resize():
	index, new = update_index()

	res =comb.Resizer(index)
	res.resize(RESIZED_DIR)


def run_all():
	equalize()
	thumbs()
	resize()
	print '\n\n\n\t\t [DONE !] '

def help():
	print '''
	============================================
	List of Arguments available:
	1. update_index - create/update index file (list of original images)
	2. equalize     - Histogram equalization of original images 
	3. thumbs       - Create and save thumbnail images in 'thumbnails/' directory
	4. resize       - Resize originl images, add white background padding and save in 'resized/' directory
	5. run_all      - Run equalize, thumbs, resize (in order)
	6. help         - show this :)
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
