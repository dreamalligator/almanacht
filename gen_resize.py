#!/usr/bin/env python

# This script generates a transparent png of the sky gazing almanac, and
# then resizes it to your liking.

from PySkyAlmanac.skyalmanac import outputAlmanac
import Image

# change the output size to your liking. i havent verified the consistency of
# output sizes for the almanac, so definitely check the properties of your
# generated png and keep the ratio when you specify the sizing.
width = 300
height = 475

filename = outputAlmanac(False, True, True) # Options: output_pdf, output_png, png_transparency
ext = '.png'
img = Image.open(filename+ext)
resized_img = img.resize((width,height),Image.ANTIALIAS)
resized_img.save(filename+'_resized'+ext)
