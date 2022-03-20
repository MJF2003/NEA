# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.uis/template.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_templateScreen(object):
    def setupUi(self, templateScreen):
        templateScreen.setObjectName("templateScreen")
        templateScreen.resize(1192, 501)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(templateScreen.sizePolicy().hasHeightForWidth())
        templateScreen.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".uis\\../../testImages/30icon.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        templateScreen.setWindowIcon(icon)
        templateScreen.setStyleSheet("\n"
"background-color: rgb(171, 171, 171)")
        templateScreen.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(templateScreen)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nav = QtWidgets.QWidget(templateScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav.sizePolicy().hasHeightForWidth())
        self.nav.setSizePolicy(sizePolicy)
        self.nav.setStyleSheet("\n"
"background-color: rgb(88, 113, 139);\n"
"color: #FFFFFF;\n"
"padding: 0.5em;\n"
"\n"
"")
        self.nav.setObjectName("nav")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.nav)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.home = QtWidgets.QPushButton(self.nav)
        self.home.setStyleSheet("")
        self.home.setCheckable(False)
        self.home.setObjectName("home")
        self.horizontalLayout.addWidget(self.home)
        self.about = QtWidgets.QPushButton(self.nav)
        self.about.setStyleSheet("")
        self.about.setObjectName("about")
        self.horizontalLayout.addWidget(self.about)
        self.title = QtWidgets.QLabel(self.nav)
        self.title.setStyleSheet("font: 75 10pt \"Comfortaa\";")
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.verticalLayout.addWidget(self.nav)

        self.retranslateUi(templateScreen)
        QtCore.QMetaObject.connectSlotsByName(templateScreen)

    def retranslateUi(self, templateScreen):
        _translate = QtCore.QCoreApplication.translate
        templateScreen.setWindowTitle(_translate("templateScreen", "Road Sign ID NEA"))
        self.home.setText(_translate("templateScreen", "Home"))
        self.about.setText(_translate("templateScreen", "About"))
        self.title.setText(_translate("templateScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Road Sign ID NEA<br />by Michael Fahey</span></p></body></html>"))
