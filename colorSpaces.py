import cv2 #import openCV2 package
import numpy as np #import numpy as short np 

input=cv2.imread('/home/akashkg/Pictures/test.jpg')

#get BGR values for pixel at 0,0 
B, G, R=input[0,0]
print ('RGB ',R,G,B)

#after converting to grayscale each pixel has only one value 0-255 range
gray_image=cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
print('grayScale ',gray_image[0,0])

# HSV values
hsv_image=cv2.cvtColor(input,cv2.COLOR_BGR2HSV)
V, S, H=hsv_image[0,0]
print ('HSV ',H,S,V)


