# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:33:45 2019

@author: Taufique
"""
import numpy as np
import cv2
pic=cv2.imread('C:/Users/monu/Pictures/Sketch.png')
dimpixel=7
color=100
space=100
filter=cv2.bilateralFilter(pic,dimpixel,color,space)

cv2.imshow('filter',filter)
cv2.waitKey(0)
cv2.destroyAllWindows()
