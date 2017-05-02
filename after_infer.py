from skimage import io, measure
import numpy as np
import matplotlib.pyplot as plt

from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour

import scipy
split_version = scipy.__version__.split('.')
if not(split_version[-1].isdigit()): # Remove dev string if present
        split_version.pop()
scipy_version = list(map(int, split_version))
new_scipy = scipy_version[0] > 0 or \
            (scipy_version[0] == 0 and scipy_version[1] >= 14)

origin = io.imread('1.jpg')
print type(origin), origin.shape
infer = io.imread('output.jpg')
print type(infer), infer.shape

contours = measure.find_contours(infer, 0.8)
print type(contours), len(contours)

# fig, ax = plt.subplots()
# ax.imshow(origin, interpolation='nearest', cmap=plt.cm.gray)

max_len = 0
max_contour = []
for n, contour in enumerate(contours):
    if len(contour) > max_len:
        max_len = len(contour)
        max_contour = contour

init = np.array(max_contour)

# ax.plot(init[:, 1], init[:, 0], linewidth=2)

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

'''
ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
'''
