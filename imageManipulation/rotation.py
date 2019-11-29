import cv2
import numpy as np 

input=cv2.imread('/home/akashkg/test_imgs/img8.png')
#store height and weight of image
height, width =input.shape[:2]

#cv2 offer rotation and scaling by the function-
#cv2.getRotationMatrix2D(rotation_centre_x, rotation_centre_y, rotation_angle, scale)

#NOTE: to rotate about centre divide height and width by 2
rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),90,1)

rotate_img=cv2.warpAffine(input,rotation_matrix,(width,height))

cv2.imshow("rotation",rotate_img)
cv2.waitKey()
cv2.destroyAllWindows()