# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:33:45 2019

@author: Taufique
"""
import numpy as np
import cv2
pic=np.zeros((500,500,3),dtype='uint8')
cv2.rectangle(pic,(0,0),(500,150),(3,200,30),3,lineType=0,shift=0)

cv2.imshow('orignal',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
