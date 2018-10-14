# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 07:26:58 2018

@author: David
"""

# Define a function
def test_waveread():
    print('Just answering you call to test_waveread function')
    

# Define a variable
EXTENSION = 'wav'


# Define a class
class WaveFile:
    def __init__(self, name, sample_rate):
        self.sample_rate = sample_rate
        self.name = name

    def wavefile_info(self):
        print("Wave file name is " + self.name)
        print(self.name + " sample rate is " + str(self.sample_rate))
        


