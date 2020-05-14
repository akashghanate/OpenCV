import cv2
import numpy as np 

input=cv2.imread('/home/akashkg/OpenCV/images/shapes.png')

#types of interpolations
# cv2.INTER_AREA - Good for shrinking or down sampling
# cv2.INTER_LINEAR - Good for zooming or up sampling
# cv2.INTER_NEAREST - fastest algo
# cv2.INTER_CUBIC - Better algo
# cv2.INTER_LANCZOS4 - Best

#for re-sizing image using cv2.resize() func-
#cv2.resize(image,dsize(output image size),xscale,yscale,interpolation)
# by default it uses INTER_LINEAR

#image 3/4 of its original image
scaled_img=cv2.resize(input,None,fx=0.75,fy=0.75)
cv2.imshow("linear interpolation",scaled_img)
cv2.waitKey()

#doubling image 
scaled_img=cv2.resize(input,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Cubic interpolation",scaled_img)
cv2.waitKey()

#to resize image to a exact dimensions
scaled_img=cv2.resize(input,(600,500),interpolation=cv2.INTER_AREA)
cv2.imshow("Skewed Size",scaled_img)
cv2.waitKey()


cv2.destroyAllWindows()
