import cv2
import numpy as np

input=cv2.imread('/home/akashkg/test_imgs/img8.png')

#store height and weight of image
height, width =input.shape[:2]

tx, ty= height/4, width/4

#    |1 0 Tx|
# T =|0 1 Ty|
# T is the translation matrix
T=np.float32([[1, 0, tx],[0, 1, ty]])

#using cv2.warpAffine for translation
img_trasnlated=cv2.warpAffine(input,T,(width,height))

cv2.imshow("Trasnlation",img_trasnlated)
cv2.waitKey()
cv2.destroyAllWindows()