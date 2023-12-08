#Copyright (c) 2023 Nikolaus Luebbert
#All rights reserved. Although I will probably give you permission to use it for whatever you want to do with it if you ask me first.

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 15 
    MIN_CHANNEL = 0
    MAX_CHANNEL = 20

    def __init__(self) -> None:
        '''
        Initalizes the varibles of a new Television object to their default values.
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        #self.__print_volume: Int

    def power(self) -> None:
        '''
        Changes the Television from on to off and vice versa.
        '''
        self.__status = not self.__status #change self.status to it's current opposite.

    def mute(self) -> None:
        '''
        Changes the mute feature of the TV from on to off and vice versa.
        Note that sucessfully running volume_up() or volume_down() will automatically unmute the TV.

        This function does nothing if the Television is off.
        '''
        if self.__status == False: #stop function if tv is currently turned off
            return
        
        self.__muted = not self.__muted #change self.muted to it's current opposite.

    def channel_up(self) -> None:
        '''
        Increases the channel number by 1.
        Note that attempting to increase the channel number past MAX_CHANNEL will cause the channel number to wrap around to MIN_CHANNEL.

        This function does nothing if the Television is off.
        '''
        if self.__status == False: #stop function if tv is currently turned off
            return
        
        
        if self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL #wrap channel around if you go over max.
        else:
            self.__channel += 1
            


    def channel_down(self) -> None:
        '''
        Decreases the channel number by 1.
        Note that attempting to decrease the channel number below MIN_CHANNEL will cause the channel number to wrap around to MAX_CHANNEL.

        This function does nothing if the Television is off.
        '''
        if self.__status == False: #stop function if tv is currently turned off
            #print("cant channel down because tv is off.")
            return
        
        if self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL #wrap channel around if you go below minimum.
        else:
            self.__channel -= 1

    def volume_up(self) -> None:
        '''
        Increases the volume by 1.
        Note that attempting to increase the volume beyond MAX_VOLUME will not change the volume.
        Note that sucessfully running volume_up() will automatically unmute the TV.

        This function does nothing if the Television is off.
        '''
        if self.__status == False: #stop function if tv is currently turned off
            return
        
        self.__muted = False #unmute if not already unmuted
        if self.__volume != Television.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        '''
        Increases the volume by 1.
        Note that attempting to increase the volume below MAX_VOLUME will not change the volume.
        Note that sucessfully running volume_down() will automatically unmute the TV.

        This function does nothing if the Television is off.
        '''
        if self.__status == False: #stop function if tv is currently turned off
            return
        
        self.__muted = False #unmute if not already unmuted
        if self.__volume != Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        '''
        Returns a status report including whether the Television is on, the current channel, and the current volume.
        Note that the volume will register as 0 if the TV is muted.
        :return: f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__print_volume}'
        '''
        if self.__muted == True:
            self.__print_volume = 0
        else:
            self.__print_volume = self.__volume

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__print_volume}'

    def power_status(self) -> bool:
        '''
        Returns a boolean to indicate whether the Television is on or off. 
        True = Television is on.
        False = Television is off.
        :return: boolean
        '''
        return self.__status

    def get_volume(self) -> int:
        '''
        Returns the current volume as an integer in the range of Television.MIN_VOLUME to Television.MAX_VOLUME
        :return: Int
        '''
        return self.__volume
    
    def get_channel(self) -> int:
        '''
        Returns the current channel as an integer in the range of Television.MIN_CHANNEL to Television.MAX_CHANNEL
        :return: int
        '''
        return self.__channel

    def get_muted(self) -> bool:
        '''
        Returns whether the Television is currently muted.
        True = The Television is muted.
        False = The Television is not muted.
        :return: bool
        '''
        return self.__muted 



    def set_channel(self, value) -> None:
        '''
        Sets the current channel directly to value. This function will do nothing if 'value' is less than Television.MIN_VOLUME or greater than Television.MAX_VOLUME.
        :param value: An integer containing the new channel for the Television.
        '''
        if self.__channel >= self.MIN_VOLUME and self.__channel <= self.MAX_VOLUME:
            self.__channel = value

    
