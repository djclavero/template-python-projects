# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 07:41:54 2018

@author: David

Script for testing 'sound' package
"""


from sound.formats import waveread

# Call function
waveread.test_waveread()

# Call variable
print('EXTENSION is ' + waveread.EXTENSION)

# Create object
soundfile = waveread.WaveFile('violin', 44100)
soundfile.wavefile_info()



