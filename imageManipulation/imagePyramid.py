#Image pyramids Scaling are useful is Object Detection
import cv2
import numpy as np 

input=cv2.imread('/home/akashkg/OpenCV/images/shapes.png')

#scaling it down to 50%
smaller=cv2.pyrDown(input)

#scaling it up to 50%
larger=cv2.pyrUp(input)

cv2.imshow("Small",smaller)
cv2.waitKey()
cv2.imshow("Large",larger)
cv2.waitKey()
cv2.destroyAllWindows()

#multiple images can be formed by looping using small/large image as input to further iterationsg