# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(395, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.chUpButton.setGeometry(QtCore.QRect(70, 10, 111, 51))
        self.chUpButton.setObjectName("chUpButton")
        self.chDownButton = QtWidgets.QPushButton(self.centralwidget)
        self.chDownButton.setGeometry(QtCore.QRect(70, 110, 101, 51))
        self.chDownButton.setObjectName("chDownButton")
        self.volUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.volUpButton.setGeometry(QtCore.QRect(130, 60, 101, 51))
        self.volUpButton.setObjectName("volUpButton")
        self.volDownButton = QtWidgets.QPushButton(self.centralwidget)
        self.volDownButton.setGeometry(QtCore.QRect(30, 60, 101, 51))
        self.volDownButton.setObjectName("volDownButton")
        self.powerButton = QtWidgets.QPushButton(self.centralwidget)
        self.powerButton.setGeometry(QtCore.QRect(290, 0, 61, 51))
        self.powerButton.setObjectName("powerButton")
        self.setFavoriteButton = QtWidgets.QPushButton(self.centralwidget)
        self.setFavoriteButton.setGeometry(QtCore.QRect(280, 400, 101, 31))
        self.setFavoriteButton.setObjectName("setFavoriteButton")
        self.muteButton = QtWidgets.QPushButton(self.centralwidget)
        self.muteButton.setGeometry(QtCore.QRect(290, 60, 61, 51))
        self.muteButton.setObjectName("muteButton")
        self.favoriteChannelsListView = QtWidgets.QListWidget(self.centralwidget)
        self.favoriteChannelsListView.setGeometry(QtCore.QRect(120, 230, 91, 192))
        self.favoriteChannelsListView.setObjectName("favoriteChannelsListView")
        self.powerLabel = QtWidgets.QLabel(self.centralwidget)
        self.powerLabel.setGeometry(QtCore.QRect(20, 200, 81, 21))
        self.powerLabel.setObjectName("powerLabel")
        self.volumeLabel = QtWidgets.QLabel(self.centralwidget)
        self.volumeLabel.setGeometry(QtCore.QRect(20, 230, 81, 21))
        self.volumeLabel.setObjectName("volumeLabel")
        self.channelLabel = QtWidgets.QLabel(self.centralwidget)
        self.channelLabel.setGeometry(QtCore.QRect(20, 260, 81, 21))
        self.channelLabel.setObjectName("channelLabel")
        self.mutedLabel = QtWidgets.QLabel(self.centralwidget)
        self.mutedLabel.setGeometry(QtCore.QRect(20, 290, 81, 21))
        self.mutedLabel.setObjectName("mutedLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 200, 291, 20))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.deleteModeRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.deleteModeRadioButton.setGeometry(QtCore.QRect(230, 350, 161, 41))
        self.deleteModeRadioButton.setObjectName("deleteModeRadioButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 220, 151, 81))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 395, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chUpButton.setText(_translate("MainWindow", "Channel Up"))
        self.chDownButton.setText(_translate("MainWindow", "Channel Down"))
        self.volUpButton.setText(_translate("MainWindow", "Volume Up"))
        self.volDownButton.setText(_translate("MainWindow", "Volume Down"))
        self.powerButton.setText(_translate("MainWindow", "Power"))
        self.setFavoriteButton.setText(_translate("MainWindow", "Set Favorite"))
        self.muteButton.setText(_translate("MainWindow", "Mute"))
        self.powerLabel.setText(_translate("MainWindow", "Power: Off"))
        self.volumeLabel.setText(_translate("MainWindow", "Volume: 0"))
        self.channelLabel.setText(_translate("MainWindow", "Channel: 0"))
        self.mutedLabel.setText(_translate("MainWindow", "Muted: No"))
        self.label.setText(_translate("MainWindow", "Double-click on a favorite to go to the channel."))
        self.deleteModeRadioButton.setText(_translate("MainWindow", "Select to Delete Mode"))
        self.label_2.setText(_translate("MainWindow", "When you are in \'Select to Delete Mode\', click on a favorite to remove it."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
