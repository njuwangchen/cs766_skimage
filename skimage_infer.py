from skimage import data, io, filters
import numpy as np
import caffe

# image = data.coins()

# edges = filters.sobel(image)

# io.imshow(edges)

filename = 'origin.jpg'
im = io.imread(filename)

in_ = np.array(im, dtype=np.float32)
in_ = in_[:,:,::-1]
in_ -= np.array((104.00698793,116.66876762,122.67891434))
in_ = in_.transpose((2,0,1))

# load net
net = caffe.Net('voc-fcn8s/deploy.prototxt', 'voc-fcn8s/fcn8s-heavy-pascal.caffemodel', caffe.TEST)
# shape for input (data blob is N x C x H x W), set data
net.blobs['data'].reshape(1, *in_.shape)
net.blobs['data'].data[...] = in_
# run net and take argmax for prediction
net.forward()
out = net.blobs['score'].data[0].argmax(axis=0)

# io.imshow(out)
# io.show()

io.imsave('output.jpg', out)
