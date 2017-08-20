from __future__ import division
from PIL import Image
import numpy as np


class Resizer:
	"""docstring for Resizer"""
	def __init__(self, index):
		self.image_paths = index

	def resize(self, save_path):
		for im in self.image_paths:
			img = Image.open(im)
			w, h = img.size
			print '[Resizing ==>', im.split('/')[-1], ']'
			new_w = 160
			new_h = int((h / w) * 160)
			
			new = img.resize((new_w, new_h), Image.BICUBIC)

			bg_l = np.zeros([new_h + 50, 25, 3], dtype=np.uint8)
			bg_r = np.zeros([new_h + 50, 25, 3], dtype=np.uint8)
			bg_u = np.zeros([25, new_w, 3], dtype=np.uint8)
			bg_d = np.zeros([25, new_w, 3], dtype=np.uint8)
			bg_l.fill(255), bg_r.fill(255), bg_u.fill(255), bg_d.fill(255)
			
			bg_l = Image.fromarray(bg_l)
			bg_d = Image.fromarray(bg_d)
			bg_r = Image.fromarray(bg_r)
			bg_u = Image.fromarray(bg_u)

			final = Image.new('RGB', ((new_w + 50), (new_h + 50)))
			final.paste(new, (25, 25))
			final.paste(bg_l, (0, 0))
			final.paste(bg_r, (new_w + 25, 0))
			final.paste(bg_u, (25, 0))
			final.paste(bg_d, (25, new_h + 25)) 
			final.save(save_path + '/' + im.split('/')[-1])


		