#Edge detection and image gradient using sobel,laplacian and canny
import cv2
import numpy as np
 
image=cv2.imread('/home/akashkg/OpenCV/images/shapes.png',0)
cv2.imshow("Original",image)
cv2.waitKey()

height, width=image.shape[:2]

#extract sobel edges
sobel_x=cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
sobel_y=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)

cv2.imshow("sobel X",sobel_x)
cv2.imshow("sobel Y",sobel_y)
cv2.waitKey()

sobel_or=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow("OR",sobel_or)
cv2.waitKey()

laplacian=cv2.Laplacian(image,cv2.CV_64F)
cv2.imshow("laplacian",laplacian)
cv2.waitKey()

#cv2.canny(image, threshold1, threshold 2) adjusting between the threshold gives proper edges
canny=cv2.Canny(image,20,170)
cv2.imshow("canny",canny)
cv2.waitKey()

cv2.destroyAllWindows()