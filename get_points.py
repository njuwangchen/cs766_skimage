from skimage_infer import infer_cnn

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

def get_points(origin):
	infer = infer(origin)
	edges = feature.canny(infer)
	label_edge, num_of_labels = label(edges, return_num=True, connectivity=2)
	points_list = []
	for i in range(1, num_of_labels+1):
		index_array = np.argwhere(np.where(label_edge == i, 1, 0))
		left_most = np.amin(index_array, axis=0)[1]
		right_most = np.amax(index_array, axis=0)[1]
		up_most = np.amin(index_array, axis=0)[0]
		down_most = np.amax(index_array, axis=0)[0]

		left_up_point = [left_most, up_most]
		left_down_point = [left_most, down_most]
		right_down_point = [right_most, down_most]
		right_up_point = [right_most, up_most]
		points_list.append(left_up_point)
		points_list.append(left_down_point)
		points_list.append(right_down_point)
		points_list.append(right_up_point)
	return np.array(points_list)

if __name__ == "__main__":
	origin = io.imread('origin.jpg')
	print get_points(origin)







