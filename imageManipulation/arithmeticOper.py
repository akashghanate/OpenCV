#Operations as add and subtract are use to vary the
#intensties of color in the image ( brightness )
import cv2
import numpy as np 

input=cv2.imread('/home/akashkg/OpenCV/images/shapes.png')
 
#create an matrix of ones with dimensions of original image
# multiple an scaler value of desired to intensify
M=np.ones(input.shape,dtype="uint8") * 75

#to see increase in brightness add the matrix using cv2.add()
added=cv2.add(input,M)
cv2.imshow("added",added)
cv2.waitKey()
cv2.destroyAllWindows()

#to see decrease in brightness subtract the matrix using cv2.subtract()
subtracted=cv2.subtract(input,M)
cv2.imshow("subtract",subtracted)
cv2.waitKey()
cv2.destroyAllWindows()
