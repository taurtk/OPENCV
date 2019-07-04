# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:33:45 2019

@author: Taufique
"""
import numpy as np
import cv2
pic=cv2.imread('C:/Users/monu/Pictures/Sketch.png')
matrix=(7,7)
blur=cv2.GaussianBlur(pic,matrix,3)

cv2.imshow('blurred',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
