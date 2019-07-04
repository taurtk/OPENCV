# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:33:45 2019

@author: Taufique
"""
import numpy as np
import cv2
pic=cv2.imread('C:/Users/monu/Pictures/Sketch.png')
kernal=3
median=cv2.medianBlur(pic,kernal)

cv2.imshow('median',median)
cv2.waitKey(0)
cv2.destroyAllWindows()
