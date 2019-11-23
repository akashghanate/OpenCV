import cv2 #import openCV2 package
import numpy as np #import numpy as short np 

input=cv2.imread('/home/akashkg/Pictures/test2.jpg')

#split image into individual channels
B, G, R=cv2.split(input)

#shows different grayscale images with intensites of R G B
cv2.imshow('RED',R)
cv2.imshow('Green',G)
cv2.imshow('Blue',B)
cv2.waitKey(0)
cv2.destroyAllWindows()

#remake merge into original using split channels
merge_image=cv2.merge([B,G,R])
cv2.imshow("Merged",merge_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#image channels can be amplified by 
# adding values to parameters in merge func

#to get individual colored images 
#create a zero matrix same size as that of input dimensions h x w using numpy
zeros=np.zeros(input.shape[:2],dtype='uint8')

cv2.imshow('Red',cv2.merge([zeros,zeros,R]))
cv2.imshow('Blue',cv2.merge([B,zeros,zeros]))
cv2.imshow('Green',cv2.merge([zeros,G,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows() 
cv2.imwrite('outputred.jpg',cv2.merge([zeros,zeros,R]))
cv2.imwrite('outputblue.jpg',cv2.merge([B,zeros,zeros]))
cv2.imwrite('outputgreen.jpg',cv2.merge([zeros,G,zeros]))