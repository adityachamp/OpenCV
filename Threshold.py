# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:21:43 2017

@author: Aditya Singh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: adityasingh
"""

def main():
    import cv2
    import numpy as np
    
    input_file = cv2.imread('Test_images/Lenna.png')
    gray = cv2.cvtColor(input_file,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Lenna_gray',gray)
    
    ret,dst=cv2.threshold(gray,127, 255, 2 );
    cv2.imshow('DST',dst)
    
    
    #binary threshold
    
    ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    cv2.imshow('Lenna_binary',thresh1)
    
    #band threshold
    
    threshold1 = 27
    threshold2 = 125
    
    ret,binary_image1 = cv2.threshold(gray,threshold1,255,cv2.THRESH_BINARY)
    ret,binary_image2 = cv2.threshold(gray,threshold2,255,cv2.THRESH_BINARY_INV)
    band_thresholded=np.bitwise_and(binary_image1, binary_image2);
    cv2.imshow('Lenna_Band_Thresh',band_thresholded)
    
    #semi
    
    ret,semi_thresholded_image=cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    semi_thresholded=np.bitwise_and( gray, semi_thresholded_image )
    cv2.imshow('Lenna_Semi',semi_thresholded)
    
    #adaptive
    
    adaptive_threshold=cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10 )
    cv2.imshow('Lenna_Adaptive',adaptive_threshold)
    
    cv2.waitKey(0)
    
if __name__=="__main__":
   main()