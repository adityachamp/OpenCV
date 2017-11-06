# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: adityasingh
"""

import cv2

input_og = cv2.imread('Test_images/Lenna.png')
[b,g,r]= cv2.split(input_og)
#print(input_og.shape)
cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red',r)
cv2.imwrite('Blue.png',b)
cv2.imwrite('Green.png',g)
cv2.imwrite('Red.png',r)


input_hsv = cv2.cvtColor(input_og, cv2.COLOR_BGR2HSV) 

[h,s,v] = cv2.split(input_hsv)

cv2.imshow('Hue',h)
cv2.imshow('Saturation',s)
cv2.imshow('Value',v)
cv2.imwrite('Hue.png',h)
cv2.imwrite('Saturation.png',s)
cv2.imwrite('Value.png',v)

input_YCRCB = cv2.cvtColor(input_og, cv2.COLOR_BGR2YCR_CB)

[y,Cb,Cr]= cv2.split(input_YCRCB)

cv2.imshow('Y',y)
cv2.imshow('Cb',Cb)
cv2.imshow('Cr',Cr)
cv2.imwrite('Y.png',y)
cv2.imwrite('Cb.png',Cb)
cv2.imwrite('Cr.png',Cr)


value= input_og[20,25]
print ('Pixel Value for RGB at [20,25] ')
print (value)

value= input_hsv[20,25]
print ('Pixel Value for HSV at [20,25] ')
print (value)


value= input_YCRCB[20,25]
print ('Pixel Value for YCrCb at [20,25] ')
print (value)


cv2.waitKey(0)
