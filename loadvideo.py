# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 02:33:45 2019

@author: Taufique
"""
import numpy as np
import cv2
cap=cv2.VideoCapture('E:/VIDEO/Paniyon Sa.mp4')
while cap.isOpened():
    ret,frame=cap.read()
    cv2.imshow('vid',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.release()
cv2.destroyAllWindows()
