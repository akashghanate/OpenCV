#segmentation - partitioning images into different regions
#contours are the continuous lines or curves that bound/cover the object completely
# contours are important in object dtetection and shape analysis

import cv2
import numpy as np

#image 
image=cv2.imread('/home/akashkg/OpenCV/images/order-copy.jpg')
cv2.imshow("original",image)
cv2.waitKey()

# grayscale image
img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#find edges
canny_img=cv2.Canny(img_gray,30,200)
cv2.imshow("edges",canny_img)
cv2.waitKey()

#finding contours cv2.findContours(image, Retrival mode, approximation mode)
# dupli=canny_img.copy()
ret,contours, hierarchy=cv2.findContours(canny_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.imshow("after contouring",canny_img)
cv2.waitKey()

#draw the contours 
#use -1 to display all contours
cv2.drawContours(image,contours,-1,(0,255,0),2)
cv2.imshow("Contours",image)
cv2.waitKey()

cv2.destroyAllWindows()
