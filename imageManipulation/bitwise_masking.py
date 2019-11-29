import cv2
import numpy as np 

#making a square in a grayscale image therefore only two dimensions
square=np.ones((500,500),dtype="uint8")
cv2.rectangle(square,(50,50),(300,300),255,-2)
cv2.imshow("sqaure",square)
cv2.waitKey()
cv2.destroyAllWindows()

#make ellipse
ellipse=np.zeros((500,500),dtype="uint8")
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-2)
cv2.imshow("ellipse",ellipse)
cv2.waitKey()
cv2.destroyAllWindows()

#masking
#intersection using bitwise_and
bitwise_and=cv2.bitwise_and(square,ellipse)
cv2.imshow("intersection",bitwise_and)
cv2.waitKey()
cv2.destroyAllWindows()

#OR using bitwise_or
bitwise_or=cv2.bitwise_or(square,ellipse)
cv2.imshow("intersection",bitwise_or)
cv2.waitKey()
cv2.destroyAllWindows()

#xor using bitwise_xor
bitwise_xor=cv2.bitwise_xor(square,ellipse)
cv2.imshow("XOR",bitwise_xor)
cv2.waitKey()
cv2.destroyAllWindows()

#invertion using bitwise_not
bitwise_not=cv2.bitwise_not(square)
cv2.imshow("invertion",bitwise_not)
cv2.waitKey()
cv2.destroyAllWindows()


