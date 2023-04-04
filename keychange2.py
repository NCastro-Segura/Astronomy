#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:05:51 2022

@author: christian
"""

from os import listdir
from os.path import isfile, join
from astropy.io import fits
from datetime import datetime 

mypath = "/home/christian/Desktop/WORK/Courses/TENERIFE/Tenerife09_M13/TEST/"
allfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(allfiles)

for file in allfiles:
    if ".fit" in file:
        print('file = ',file,': ' , end=' ')

        hdu = fits.open(mypath+file,mode='update')
        hdr = hdu[0].header
        #print(hdr)
        date_str = hdr['DATEOBS']
        date_str = '2022-4-6'
        date = datetime.strptime(date_str, '%Y-%m-%d')
        #this is a bit of a hack -- the %m and %d formats "officially" 
        #assume zero padding, but seem to work OK even if the numbers
        #are not zero padded. So we can exploit this to convert from 
        #non-zero-padded to zeropadded
        date_str_new = date.strftime('%Y-%m-%d')
        #hdr.set('UT-STRT', start_time)
        print('converting date from ', date_str, '  to ', date_str_new)
        #print(hdr)
        #start_time = hdr['UT-START']
        hdr.set('DATEOBS', date_str_new)
        hdu.flush()
        
        