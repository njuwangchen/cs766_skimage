from skimage import io, measure, feature
import numpy as np
import matplotlib.pyplot as plt

from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour

from skimage.feature import corner_harris, corner_subpix, corner_peaks
from skimage.transform import warp, AffineTransform

from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

import matplotlib.patches as mpatches

import scipy
split_version = scipy.__version__.split('.')
if not(split_version[-1].isdigit()): # Remove dev string if present
        split_version.pop()
scipy_version = list(map(int, split_version))
new_scipy = scipy_version[0] > 0 or \
            (scipy_version[0] == 0 and scipy_version[1] >= 14)

origin = io.imread('origin.jpg')
print type(origin), origin.shape
infer = io.imread('output.jpg')
print type(infer), infer.shape

edges = feature.canny(infer)
print type(edges), edges.shape

'''
index_array = np.argwhere(edges)
print type(index_array), index_array.shape
'''

label_image = label(infer, connectivity=2)
'''
image_label_overlay = label2rgb(label_image, image=origin)

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(image_label_overlay)

for region in regionprops(infer):
    # take regions with large enough areas
    # draw rectangle around segmented coins
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(rect)

ax.set_axis_off()
plt.tight_layout()
plt.show()
'''
'''
image = edges

coords = corner_peaks(corner_harris(image), min_distance=5)
coords_subpix = corner_subpix(image, coords, window_size=13)

fig, ax = plt.subplots()
ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)
ax.plot(coords[:, 1], coords[:, 0], '.b', markersize=3)
ax.plot(coords_subpix[:, 1], coords_subpix[:, 0], '+r', markersize=15)
ax.axis((0, 350, 350, 0))
plt.show()
'''

label_edge, num_of_labels = label(edges, return_num=True, connectivity=2)
print num_of_labels

index_array_1 = np.argwhere(np.where(label_edge == 1, 1, 0))
print type(index_array_1), index_array_1.shape

index_array_2 = np.argwhere(np.where(label_edge == 2, 1, 0))
print type(index_array_2), index_array_2.shape

'''
fig, ax = plt.subplots()
ax.scatter(index_array_1[:, 1], index_array_1[:, 0])
plt.show()
'''

'''
contours = measure.find_contours(edges, 0.8)
print type(contours), len(contours)

fig, ax = plt.subplots()
ax.imshow(origin, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
'''
'''
max_len = 0
max_contour = []
for n, contour in enumerate(contours):
    if len(contour) > max_len:
        max_len = len(contour)
        max_contour = contour

init = np.array(max_contour)
'''

fig, ax = plt.subplots()
init = index_array_1

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])

img = rgb2gray(origin)

if not new_scipy:
    print('You are using an old version of scipy. '
          'Active contours is implemented for scipy versions '
          '0.14.0 and above.')

if new_scipy:
    snake = active_contour(img, init)

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111)
    plt.gray()
    ax.imshow(img)
    ax.plot(init[:, 1], init[:, 0], '--r', lw=3)
    ax.plot(snake[:, 1], snake[:, 0], '-b', lw=3)
    ax.set_xticks([]), ax.set_yticks([])
    ax.axis([0, img.shape[1], img.shape[0], 0])
    plt.show()
