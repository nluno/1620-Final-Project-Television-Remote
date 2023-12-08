#Copyright (c) 2023 Nikolaus Luebbert
#All rights reserved. Although I will probably give you permission to use it for whatever you want to do with it if you ask me first.
from PyQt5.QtWidgets import * #QMainWindow
from gui import *
from television import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.currTelevision = Television()
        
        self.favoritesList = []
        
        #Connecting Buttons:
        self.powerButton.clicked.connect(lambda : self.powerButtonHandler())
        self.muteButton.clicked.connect(lambda : self.muteButtonHandler())

        #deleteModeRadioButton
        self.chUpButton.clicked.connect(lambda : self.chUpHandler())
        self.chDownButton.clicked.connect(lambda : self.chDownHandler())
        self.volUpButton.clicked.connect(lambda : self.volUpHandler())
        self.volDownButton.clicked.connect(lambda : self.volDownHandler())

        self.favoriteChannelsListView.itemActivated.connect(self.favoriteSelected)
        self.setFavoriteButton.clicked.connect(lambda : self.setFavoriteHandler())

    def powerButtonHandler(self):
        self.currTelevision.power()
        self.updateInterface()
        

    def muteButtonHandler(self):
        self.currTelevision.mute()
        self.updateInterface()
        
    def volUpHandler(self):
        self.currTelevision.volume_up()
        self.updateInterface()

    def volDownHandler(self):
        self.currTelevision.volume_down()
        self.updateInterface()

    def chUpHandler(self):
        self.currTelevision.channel_up()
        self.updateInterface()

    def chDownHandler(self):
        self.currTelevision.channel_down()
        self.updateInterface()

    def setFavoriteHandler(self):
        #There isn't much use in adding zeroes to the favorites list when the TV is turned off. Therefore adding to favorites is disabled when the TV is off.
        if self.currTelevision.power_status() != False:
            self.favoritesList = []
            self.favoritesList.append(str(self.currTelevision.get_channel())) #turn the current channel number to a string, and add it to the favorites list
            self.favoriteChannelsListView.addItems(self.favoritesList)  #display it to the list. 
        
    def favoriteSelected(self, item):
        self.powerStatus = self.currTelevision.power_status()

        #It seems like a reasonable assumption that you can remove the settings stored in the RAM of a TV remote even when the television itself is powered off.
        if self.deleteModeRadioButton.isChecked() == True:
               item.setHidden(True)
        elif self.powerStatus == True: #You shouldn't be able to change the channel if the TV is off. 
            self.currTelevision.set_channel(int(item.text()))

        self.updateInterface()


    def updateInterface(self):
        self.powerStatus = self.currTelevision.power_status()

        if self.powerStatus == True:
            self.powerLabel.setText("Power: On")
        else:
            self.powerLabel.setText("Power: Off")
            
        
        self.volumeLabel.setText('Volume: {}'.format(self.currTelevision.get_volume()))
        self.channelLabel.setText('Channel: {}'.format(self.currTelevision.get_channel()))

        if self.currTelevision.get_muted() == True:
            self.mutedLabel.setText("Muted: Yes")
        else:
            self.mutedLabel.setText("Muted: No")
            
        #self.mutedLabel.setText('Muted: {}'.format(self.currTelevision.get_muted()))
            
