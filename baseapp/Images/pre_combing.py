from __future__ import division
from PIL import Image
from os import walk
from sys import argv, exit
from time import time

ORIGINAL_IMAGE_PATH = "original/"
THUMBNAIL_PATH = "thumbnails/"
MOD_PATH = "modified/"
RES_PATH = "resized/"


def list_original_images():
	"""Creates list of original images.
		
		return type <list> 
	"""
	for(dirpath, dirname, filename) in walk(ORIGINAL_IMAGE_PATH):
		images = [ORIGINAL_IMAGE_PATH + img for img in filename]

	return images
	

def	save_thumbnails(image_list):
	"""Saves thumbnail images.

	"""
	size = 256, 256
	for im in image_list:
		img = Image.open(im)
		img.thumbnail(size)
		img.save((THUMBNAIL_PATH + im[im.rfind('/') + 1:]), "JPEG")


def save_modified(image_list):
	"""Save modified images.
		
		Small image size improve search performances
		Added white background to improve foreground color extraction
	"""
	for im in image_list:
		img = Image.open(im)
		w, h = img.size
		new_w = 160
		new_h = int((h / w) * 160) 
		new = img.resize((new_w, new_h), Image.BICUBIC)
		
		# Add extra white layer
		white_bg = Image.open('WHITE_BG.png')

		# create new image
		final = Image.new('RGB', (160, (new_h + 100)))
		final.paste(white_bg, (0, 0))
		final.paste(new, (0, 100)) 
		final.save(MOD_PATH + im[im.rfind('/') + 1:])	


def save_resized(image_list):
	"""Save modified images.
		
		Small image size improve search performances
		Added white background to improve foreground color extraction
	"""
	for im in image_list:
		img = Image.open(im)
		w, h = img.size
		new_w = 160
		new_h = int((h / w) * 160) 
		new = img.resize((new_w, new_h), Image.BICUBIC)
		
		new.save(RES_PATH + im[im.rfind('/') + 1:])	



if __name__ == '__main__':
	if len(argv) != 2:
		print 'Nothing to do! No arg'
		exit(0)
	t1 = time()
	image_list = list_original_images()
	if argv[1] == 'mod':
		save_modified(image_list)
	elif argv[1] == 'thumb':
		save_thumbnails(image_list)
	elif argv[1] == 'res':
		save_resized(image_list)
	print "DONE !!"
	print "Time Taken [", (time() - t1), " secs]" 
