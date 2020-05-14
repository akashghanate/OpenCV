#it's opposite to blurring, it strengthens the edges
import cv2
import numpy as np 

input=cv2.imread('/home/akashkg/OpenCV/images/shapes.png')

# kernel= |-1 -1 -1 |
#         |-1  9 -1 |
#         |-1 -1 -1 |
# it sums up to 1

kernel=np.array([[-1,-1,-1],
                 [-1, 9,-1],
                 [-1,-1,-1]])

sharpened=cv2.filter2D(input,-1,kernel)
cv2.imshow("sharpening",sharpened)
cv2.waitKey()
cv2.destroyAllWindows()