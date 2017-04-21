import os
import sys
import numpy as np
import scipy.misc
from PIL import Image
from PyQt4 import QtCore, QtGui
import ads
import warp_ads
from get_points import get_points
from skimage import img_as_float

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class adsDialog(QtGui.QMainWindow, ads.Ui_AdsApp):

    img_width = 480
    img_height = 640

    ads_width = 240
    ads_height = 320


    oriImgData = np.zeros(shape=(img_height,img_width))
    hasImage = False

    adsData = np.zeros(shape=(ads_height, ads_width))
    hasAds = False

    outputImgData = np.zeros(shape=(img_height, img_width))
    hasOutput = False


    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # set upload image button
        self.uploadImgBtn.clicked.connect(self.select_image)

        # set upload ads button
        self.uploadAdsBtn.clicked.connect(self.select_ads)

        # set quit button
        self.quitBtn.clicked.connect(self.close)

        # set advertising button
        self.genAds.clicked.connect(self.advertising)



    def select_image(self):
        # open image
        filename = QtGui.QFileDialog.getOpenFileName(self, 'open file',
                os.getcwd(), "Images (*.png *.jpg)")
        print ("open: " + filename)

        # display
        pixMap = QtGui.QPixmap(_fromUtf8(filename))
        scaledPixMap = pixMap.scaled(self.oriImg.size(), QtCore.Qt.KeepAspectRatio)
        self.oriImg.setPixmap(scaledPixMap)

        # load data
        self.riImgData = self.load_image(str(filename), 1)
        self.hasImage = True

    def select_ads(self):
        # open image
        filename = QtGui.QFileDialog.getOpenFileName(self, 'open file',
                os.getcwd(), "Images (*.png *.jpg)")
        print ("open: " + filename)

        # display
        pixMap = QtGui.QPixmap(_fromUtf8(filename))
        scaledPixMap = pixMap.scaled(self.ads.size(), QtCore.Qt.KeepAspectRatio)
        self.ads.setPixmap(scaledPixMap)
        self.hasAds = True

        # load data
        self.adsData = self.load_image(str(filename), 2)
        self.hasAds = True


    def advertising(self):
        if (not self.hasImage):
            print ("No input image!")
            return
        if (not self.hasAds):
            print ("No input ads!")
            return

        # train and get the area of the monitor
        src = get_points(self.oriImgData)
        print (src)

        # warp ads
        src = src[0:4]
        warp = warp_ads.warpAds()
        self.outputImgData = warp.warp_ads(img_as_float(self.oriImgData),img_as_float(self.adsData), src)
        self.hasOutput = True

        self.save_image("after_advertising.jpg")


    def load_image(self, filename, flag):
        img = Image.open(filename)
        img.load()
        data = np.asarray(img, dtype = "int32")
        if (flag == 1):
            scipy.misc.imresize(data, (self.img_height, self.img_width))
        else:
            scipy.misc.imresize(data, (self.ads_height, self.ads_width))
        return data


    def save_image(self, filename):
        if (not self.hasOutput):
            print ("No output to save!")
            return

        img = Image.fromarray(self.outputImgData)
        img.save(filename)



def main():
    app = QtGui.QApplication(sys.argv)
    myapp = adsDialog()
    myapp.show()
    sys.exit(app.exec_())
'''
def test():
    app = QtGui.QApplication(sys.argv)
    myapp =
'''

if __name__ == "__main__":
    main()
