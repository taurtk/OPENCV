# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:33:45 2019

@author: Taufique
"""
import numpy as np
import cv2
pic=np.zeros((500,500,3),dtype='uint8')
cv2.line(pic,(350,350),(500,350),(0,65,25))

cv2.imshow('orignal',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
