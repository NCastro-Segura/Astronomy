#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:05:51 2022

@author: christian
"""

from os import listdir
from os.path import isfile, join
from astropy.io import fits

mypath = "/home/christian/Desktop/WORK/Courses/TENERIFE/Tenerife09_M13/TEST/"
allfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(allfiles)

for file in allfiles:
    if ".fits" in file:
        print(file)

        hdu = fits.open(mypath+file,mode='update')
        hdr = hdu[0].header
        start_time = hdr['EXP-STRT']
        hdr.set('UT-STRT', start_time)
        #print(hdr)
        #start_time = hdr['UT-START']
        #hdr.set('EXP-STRT', start_time)
        hdu.flush()
        