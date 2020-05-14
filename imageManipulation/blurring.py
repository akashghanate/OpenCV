import cv2
import numpy as np 

input=cv2.imread('/home/akashkg/OpenCV/images/shapes.png')
cv2.imshow("Original",input)
cv2.waitKey()
cv2.destroyAllWindows()
 
#convolutions are done on a kernel of some m*n matrix pixel of the original image size
kernel3x3=np.ones((3,3),np.float32)/9

#use cv2.filter2D() to convolve with the kernel
blurred=cv2.filter2D(input,-1,kernel3x3)
cv2.imshow("kernel3x3",blurred)
cv2.waitKey()
cv2.destroyAllWindows()

#box blur
blurred=cv2.blur(input,(3,3))
cv2.imshow("Averaging",blurred)
cv2.waitKey()
cv2.destroyAllWindows()

#Gaussian filter
blurred=cv2.GaussianBlur(input,(7,7),0)
cv2.imshow("Gaussian",blurred)
cv2.waitKey()
cv2.destroyAllWindows()

#median blur takes median of all the pixels under kernel area
blurred=cv2.medianBlur(input,5)
cv2.imshow("Median Blur",blurred)
cv2.waitKey()
cv2.destroyAllWindows()

#bilateral blur is noise removal while keeping edges sharp
blurred=cv2.bilateralFilter(input,9,75,75)
cv2.imshow("Bilateral Blur",blurred)
cv2.waitKey()
cv2.destroyAllWindows()



