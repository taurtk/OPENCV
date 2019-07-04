# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:33:45 2019

@author: Taufique
"""
import numpy as np
import cv2
pic=cv2.imread('C:/Users/monu/Pictures/Sketch.png',0)
threshold_value=100
(T_value, binary_threshold)=cv2.threshold(pic, threshold_value, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('rotate',binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
