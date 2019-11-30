#Dilation - adds pixel to the boundaries of the object in an image
#Erosion - removes pixel at the boundaries of the object in an image
#Opening - Errosion followed by dilation
#Closing - Dilation followed by errosion

import cv2
import numpy as np
 
input=cv2.imread('/home/akashkg/test_imgs/img9.jpg')
cv2.imshow("Original",input)
cv2.waitKey()

#let's define a kernel
kernel=np.ones((3,3),np.uint8)

#erosion using cv2.erode
erosion=cv2.erode(input,kernel,iterations=1)
cv2.imshow("Erosion",erosion)
cv2.waitKey()

#dilation using cv2.dilate()
dilation=cv2.dilate(input,kernel,iterations=1)
cv2.imshow("Dilation",dilation)
cv2.waitKey()

#opening using morphologyEx
opening=cv2.morphologyEx(input,cv2.MORPH_OPEN,kernel)
cv2.imshow("opening",opening)
cv2.waitKey()

#closing using morphologyEx
closing=cv2.morphologyEx(input,cv2.MORPH_CLOSE,kernel)
cv2.imshow("Closing",closing)
cv2.waitKey()


cv2.destroyAllWindows()