import cv2 #import openCV2 package
import numpy as np #import numpy as short np 

#load an image into variable input using imread giving the path 
input=cv2.imread('/home/akashkg/Pictures/test.jpg')

#to display image loaded into input we use imshow 
#first parameter is window name and second is image variable
cv2.imshow('TestWindow',input)

#allows to input info when a image window is open by leaving it blank
#waits for anykey to be pressed before continuing
cv2.waitKey()

# closes all open windows without with the program hangs
cv2.destroyAllWindows()      

#shows how image is stored with dimension of image
# and 3L saying it has RGB values
print (input.shape)

#isolating the height and width of image
print('Height',input.shape[0])
print('Width',input.shape[1])

#saving images using imwrite
cv2.imwrite('output.jpg',input)
cv2.imwrite('output.png',input)
