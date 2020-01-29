# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 23:48:54 2020

@author: acer
"""
import pandas as pd
songs = pd.Series([10,20,30,40],index = ['nitin','abhi','vyom','akash'],name='English')
print(songs)
mask = songs < songs.mean()
print(mask)
print(songs[mask])