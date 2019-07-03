# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:33:45 2019

@author: Taufique
"""
import numpy as np
import cv2
pic=cv2.imread('C:/Users/monu/Pictures/Sketch.png')
cols=pic.shape[1]
rows=pic.shape[0]

M=np.float32([[1,0,-158],[0,1,-70]])
shifted=cv2.warpAffine(pic,M,(cols,rows))
cv2.imshow('shifted',shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
