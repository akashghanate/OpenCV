import cv2 #import openCV2 package
import numpy as np #import numpy as short np 

input=cv2.imread('/home/akashkg/Pictures/test.jpg')
cv2.imshow('TestWindow',input)
cv2.waitKey()

#using cvtColor to convert to grayscale
gray_image=cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)

cv2.imshow('GrayScale',gray_image)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('output.jpg',gray_image)
#short code to covert
# input=cv2.imread('/home/akashkg/Pictures/test.jpg',0)

