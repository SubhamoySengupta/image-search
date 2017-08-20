from __future__ import division
from PIL import Image

def	save_thumbnails(image_list, save_path):
	"""Saves thumbnail images.

	"""
	# size = 256, 256
	for im in image_list:
		img = Image.open(im)
		w, h = img.size
		print '[Resizing ==>', im.split('/')[-1], ']'
		new_w = 128
		new_h = int((h / w) * 128)
		new = img.resize((new_w, new_h), Image.BICUBIC)
		print '[Saving ' + im.split('/')[-1]+ ']'
		new.save((save_path + '/' + im.split('/')[-1]), "JPEG")