import json
from sklearn.neighbors import NearestNeighbors
from sys import argv
import cv2
from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = BASE_DIR + '/Images/modified/'

default_im_name = 'Adidas-Yeezy-Boost-750-Triple-Black.jpg'
path = IMAGE_DIR
out_path = BASE_DIR + '/Images/original/'

def centroid_histogram(clt):
	# grab the number of different cluster and create a histogram
	# based on the number of pixels assigned to each cluster
	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins=numLabels)

	# normalize the histogram such that it sums to one
	hist = hist.astype('float')
	hist /= hist.sum()

	return hist


if len(argv) == 2:
	img_path = path + argv[1]
else:
	img_path = path + default_im_name

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_org = img.copy()
# cluster the pixel intensities
clt = KMeans(n_clusters=3)
# reshape the image to be a list of RGB pixels rather than M * N array
img = img.reshape((img.shape[0] * img.shape[1], 3))
clt.fit(img)
hist = centroid_histogram(clt)
h = list(hist)
c = list(clt.cluster_centers_)
del c[h.index(max(h))]
del h[h.index(max(h))]
h = [(i/sum(h)) for i in h]

if h[1] > h[0]:
	h[0], h[1] = h[1], h[0]
	c[0], c[1] = c[1], c[0]	

test_data = c[0].astype('uint8').tolist()
test_pc = c[1].astype('uint8').tolist()

f = open('data/color_dat.json', 'r')

dat = json.loads(f.read())

cd_primary = dat['c_list']['primary']
cd_secondary = dat['c_list']['secondary']
cd_pc = dat['pc_list']

# knn object
neigh = NearestNeighbors(n_neighbors=10, radius=0.1)

neigh.fit(cd_primary)
b1=neigh.kneighbors([test_data])
for i in b1:
	print i
for i in b1[1][0]:	
	print cd_primary[i]

print b1[1][0][0]




# knn object
neigh = NearestNeighbors(n_neighbors=10, radius=0.1)

neigh.fit(cd_secondary)
b2=neigh.kneighbors([test_pc])
for i in b2:
	print i
for i in b2[1][0]:	
	print cd_secondary[i]

print b2[1][0][0]




a1 = out_path + dat['data'][b1[1][0][0]]['name']
a2 = out_path + dat['data'][b1[1][0][1]]['name']
a3 = out_path + dat['data'][b1[1][0][2]]['name']
a4 = out_path + dat['data'][b1[1][0][3]]['name']
a5 = out_path + dat['data'][b1[1][0][4]]['name']
a6 = out_path + dat['data'][b1[1][0][5]]['name']
a7 = out_path + dat['data'][b1[1][0][6]]['name']
a8 = out_path + dat['data'][b1[1][0][7]]['name']

a1 = cv2.imread(a1)
a2 = cv2.imread(a2)
a3 = cv2.imread(a3)
a4 = cv2.imread(a4)
a5 = cv2.imread(a5)
a6 = cv2.imread(a6)
a7 = cv2.imread(a7)
a8 = cv2.imread(a8)

a1 = cv2.cvtColor(a1, cv2.COLOR_BGR2RGB)
a2 = cv2.cvtColor(a2, cv2.COLOR_BGR2RGB)
a3 = cv2.cvtColor(a3, cv2.COLOR_BGR2RGB)
a4 = cv2.cvtColor(a4, cv2.COLOR_BGR2RGB)
a5 = cv2.cvtColor(a5, cv2.COLOR_BGR2RGB)
a6 = cv2.cvtColor(a6, cv2.COLOR_BGR2RGB)
a7 = cv2.cvtColor(a7, cv2.COLOR_BGR2RGB)
a8 = cv2.cvtColor(a8, cv2.COLOR_BGR2RGB)


fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(nrows=1, ncols=8, figsize=(10, 10),
                                    sharex=True, sharey=True)

ax1.imshow(a1)
ax1.axis('off')
ax2.imshow(a2)
ax2.axis('off')
ax3.imshow(a3)
ax3.axis('off')
ax4.imshow(a4)
ax4.axis('off')
ax5.imshow(a5)
ax5.axis('off')
ax6.imshow(a6)
ax6.axis('off')
ax7.imshow(a7)
ax7.axis('off')
ax8.imshow(a8)
ax8.axis('off')

# plt.subplot(121)
# plt.imshow(a1)
# plt.xticks([]), plt.yticks([])
# plt.subplot(122)
# plt.imshow(a3)
# plt.xticks([]), plt.yticks([])
# plt.subplot(123)
# plt.imshow(a3)
fig.tight_layout()
plt.show()

# a1 = out_path + dat['data'][b2[1][0][0]]['name']
# a2 = out_path + dat['data'][b2[1][0][1]]['name']
# a3 = out_path + dat['data'][b2[1][0][2]]['name']
# a4 = out_path + dat['data'][b2[1][0][3]]['name']

# a1 = cv2.imread(a1)
# a2 = cv2.imread(a2)
# a3 = cv2.imread(a3)
# a4 = cv2.imread(a4)

# a1 = cv2.cvtColor(a1, cv2.COLOR_BGR2RGB)
# a2 = cv2.cvtColor(a2, cv2.COLOR_BGR2RGB)
# a3 = cv2.cvtColor(a3, cv2.COLOR_BGR2RGB)
# a4 = cv2.cvtColor(a4, cv2.COLOR_BGR2RGB)

# plt.subplot(121)
# plt.imshow(a1)
# plt.xticks([]), plt.yticks([])
# plt.subplot(122)
# plt.imshow(a2)
# plt.xticks([]), plt.yticks([])
# # plt.subplot(123)
# # plt.imshow(a3)
# plt.show()

# print '\n\n\n'
