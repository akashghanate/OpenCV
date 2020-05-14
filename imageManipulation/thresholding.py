#thresholding is converting an image into it's binary form
#cv2.threshold(image, Threshold value, Max value, Threshold type)
 
#NOTE: image is first converted to grayscale before thresholding

import cv2
import numpy as np 
 
# threshold types
# cv2.THRESH_BINARY
# cv2.THRESH_BINARY_INV
# cv2.THRESH_TRUNC
# cv2.THRESH_TOZERO
# cv2.THRESH_TOZERO_INV

input=cv2.imread('/home/akashkg/OpenCV/images/shapes.png',0)
cv2.imshow("Original",input)
cv2.waitKey()

#vlaues below 127 goes to 0 (black) everything above goes to 255 (white)
ret,thres=cv2.threshold(input,127,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary",thres)
cv2.waitKey()

#vlaues below 127 goes to 255 everything above goes to 0 (reverse of above)
ret,thres=cv2.threshold(input,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse",thres)
cv2.waitKey()

#vlaues above 127 are truncated (held) at 127   
ret,thres=cv2.threshold(input,127,255,cv2.THRESH_TRUNC)
cv2.imshow("Threshold TRUNC",thres)
cv2.waitKey()

#vlaues below 127 goes to 0, above are unchanged   
ret,thres=cv2.threshold(input,127,255,cv2.THRESH_TOZERO)
cv2.imshow("Threshold TOZERO",thres)
cv2.waitKey()

#vlaues below 127 are unchanged , above goes to 0  
ret,thres=cv2.threshold(input,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("Threshold TOZERO Inverse",thres)
cv2.waitKey()

cv2.destroyAllWindows()

#better way is using adaptive thresholding