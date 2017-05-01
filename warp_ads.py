
import numpy as np
from skimage import transform as tf
from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from PIL import Image
from scipy import ndimage
from skimage import img_as_float

debug = False

class warpAds:

    def __init__(self):
        # mask for ads image
        self.mask_ads = None
        self.mask_img = None


    def warp_ads(self, img, ads, src):
        ads_width = ads.shape[1]
        ads_height = ads.shape[0]
        ads = self.remove_all_zero_pix(ads)
        dst = np.array([[0, 0], [0, ads_height], [ads_width, ads_height], [ads_width, 0]])

        img_width = img.shape[1]
        img_height = img.shape[0]
        rotated = self.geo_transform(src, dst, ads, (img_height, img_width))

        output = self.merge_img(img, rotated)
        return output

    def remove_all_zero_pix(self, img):
        mask = img[:,:,0] + img[:,:,1] + img[:,:,2]
        mask_3d = np.stack((mask, mask, mask), axis=-1)
        new_img = img
        new_img[mask_3d==0] = 0.000001
        return new_img

    """
    do ads tranformation
    """
    def geo_transform(self, src, dst, ads, imgSize):

        tform = tf.ProjectiveTransform()
        tform.estimate(src, dst)

        if(debug):
            print src
            print dst

        # rotate
        rotated = tf.warp(ads, tform, output_shape=imgSize)

        # set mask
        self.set_mask(rotated[:,:,0] + rotated[:,:,1] + rotated[:,:,2])

        if(debug):
            print self.mask_ads
            print self.mask_ads.shape

        return rotated

    '''
    img1: image
    img2: ads
    '''
    def merge_img(self, img1, img2):

        mask1 = np.stack((self.mask_img, self.mask_img, self.mask_img), axis=-1)
        mask2 = np.stack((self.mask_ads, self.mask_ads, self.mask_ads), axis=-1)


        output_img = img1 * mask1 + img2 * mask2
        #print type(img1[0,0,0]), type(img2[0,0,0]), type(mask1[0,0,0]), type(mask2[0,0,0])
        #self.draw(img2)
        #self.draw(mask2)
        return output_img

    def set_mask(self, img_bw):
        mask_ads = np.zeros(shape=img_bw.shape)
        np.copyto(mask_ads, img_bw)
        mask_ads[mask_ads > 0] = 1
        mask_ads.astype(float)

        self.mask_ads = self.get_blur_mask(mask_ads, 5)

        mask_img = np.zeros(shape=img_bw.shape)
        mask_img = 1 - mask_ads
        '''
        np.copyto(mask_img, mask_ads)
        mask_img[mask_ads == 1] = 0
        mask_img[mask_ads == 0] = 1
        '''
        self.mask_img = mask_img


    def get_blur_mask(self, mask, thres):
        # get distance
        mask_dist = ndimage.distance_transform_edt(mask)
        mask_dist[mask_dist > thres] = thres
        mask_dist = mask_dist / thres
        return mask_dist


    def draw(self, img):
        imgplot = plt.imshow(img)
        plt.show()


def test():
    #np.set_printoptions(threshold='nan')

    ads = io.imread('ads2.png')
    ads_float = img_as_float(ads)

    # src are the corner points in the source image
    #src = np.array([[50, 50], [25, 100], [200, 200], [400, 0]])
    src = np.array([[56, 100], [56, 186], [194, 178], [192, 97]])

    # merge
    img = io.imread('origin.jpg')
    img_float = img_as_float(img)

    test = warpAds()
    output = test.warp_ads(img_float, ads_float, src)

    test.draw(output)
    #test.draw(test.mask_img)
    #test.draw(test.mask_ads)

def test_blur_mask():
    mask = np.array([[0,1,1,1,1], [0,0,1,1,1], [0,1,1,1,1], [0,1,1,1,0], [0,1,1,0,0]])
    test = warpAds()
    new_mask = test.get_blur_mask(mask, 2)
    print new_mask

if __name__ == "__main__":
    test()
    #test_blur_mask()


