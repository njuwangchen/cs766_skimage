from skimage import data, io, filters
import numpy as np
import caffe
import sys

def infer_cnn(im):
        print type(im), im.shape
        in_ = np.array(im, dtype=np.float32)
	in_ = in_[:,:,::-1]
	in_ -= np.array((104.00698793,116.66876762,122.67891434))
	in_ = in_.transpose((2,0,1))

	# load net
	net = caffe.Net('deploy.prototxt', 'fcn8s.caffemodel', caffe.TEST)
	# shape for input (data blob is N x C x H x W), set data
	net.blobs['data'].reshape(1, *in_.shape)
	net.blobs['data'].data[...] = in_
	# run net and take argmax for prediction
	net.forward()
	out = net.blobs['score'].data[0].argmax(axis=0)

	io.imsave('output.jpg', out)
	return np.array(out, float)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python skimage_infer.py image_name"
        exit()
    im = io.imread(sys.argv[1])
    infer_cnn(im)
