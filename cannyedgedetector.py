# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:33:45 2019

@author: Taufique
"""
import numpy as np
import cv2
pic=cv2.imread('C:/Users/monu/Pictures/Sketch.png')
thresholdval1=50
thresholdval2=100
canny = cv2.Canny(pic, thresholdval1, thresholdval2)

cv2.imshow('canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
