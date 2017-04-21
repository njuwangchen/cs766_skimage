# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ads.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AdsApp(object):
    def setupUi(self, AdsApp):
        AdsApp.setObjectName(_fromUtf8("AdsApp"))
        AdsApp.resize(946, 652)
        self.verticalLayoutWidget_2 = QtGui.QWidget(AdsApp)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(530, 20, 401, 401))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.adsImgLay = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.adsImgLay.setObjectName(_fromUtf8("adsImgLay"))
        self.adsImg = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.adsImg.setAlignment(QtCore.Qt.AlignCenter)
        self.adsImg.setObjectName(_fromUtf8("adsImg"))
        self.adsImgLay.addWidget(self.adsImg)
        self.uploadImgBtn = QtGui.QPushButton(AdsApp)
        self.uploadImgBtn.setGeometry(QtCore.QRect(100, 490, 171, 31))
        self.uploadImgBtn.setObjectName(_fromUtf8("uploadImgBtn"))
        self.genAds = QtGui.QCommandLinkButton(AdsApp)
        self.genAds.setGeometry(QtCore.QRect(420, 210, 101, 31))
        self.genAds.setObjectName(_fromUtf8("genAds"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(AdsApp)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 401, 401))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.oriImgLay = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.oriImgLay.setObjectName(_fromUtf8("oriImgLay"))
        self.oriImg = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.oriImg.setAlignment(QtCore.Qt.AlignCenter)
        self.oriImg.setObjectName(_fromUtf8("oriImg"))
        self.oriImgLay.addWidget(self.oriImg)
        self.uploadAdsBtn = QtGui.QPushButton(AdsApp)
        self.uploadAdsBtn.setGeometry(QtCore.QRect(100, 570, 171, 31))
        self.uploadAdsBtn.setObjectName(_fromUtf8("uploadAdsBtn"))
        self.progressBar = QtGui.QProgressBar(AdsApp)
        self.progressBar.setGeometry(QtCore.QRect(300, 440, 321, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.quitBtn = QtGui.QPushButton(AdsApp)
        self.quitBtn.setGeometry(QtCore.QRect(690, 570, 171, 31))
        self.quitBtn.setObjectName(_fromUtf8("quitBtn"))
        self.verticalLayoutWidget = QtGui.QWidget(AdsApp)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(390, 470, 161, 161))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.adsLay = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.adsLay.setObjectName(_fromUtf8("adsLay"))
        self.ads = QtGui.QLabel(self.verticalLayoutWidget)
        self.ads.setAlignment(QtCore.Qt.AlignCenter)
        self.ads.setObjectName(_fromUtf8("ads"))
        self.adsLay.addWidget(self.ads)
        self.saveAds = QtGui.QPushButton(AdsApp)
        self.saveAds.setGeometry(QtCore.QRect(690, 500, 171, 31))
        self.saveAds.setObjectName(_fromUtf8("saveAds"))

        self.retranslateUi(AdsApp)
        QtCore.QMetaObject.connectSlotsByName(AdsApp)

    def retranslateUi(self, AdsApp):
        AdsApp.setWindowTitle(_translate("AdsApp", "Dialog", None))
        self.adsImg.setText(_translate("AdsApp", "After advertising", None))
        self.uploadImgBtn.setText(_translate("AdsApp", "Upload Image", None))
        self.genAds.setText(_translate("AdsApp", "Advertising", None))
        self.oriImg.setText(_translate("AdsApp", "Please upload image", None))
        self.uploadAdsBtn.setText(_translate("AdsApp", "Upload Ads", None))
        self.quitBtn.setText(_translate("AdsApp", "Quit", None))
        self.ads.setText(_translate("AdsApp", "Please upload Ads", None))
        self.saveAds.setText(_translate("AdsApp", "Save Ads Image", None))

