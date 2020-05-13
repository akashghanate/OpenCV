import cv2
import numpy as np 
 
#create a black image
image=np.zeros((512,512,3),np.uint8)

#draw a diagonal line blue and thickness 5 pixel
cv2.line(image,(0,0),(511,511),(255,0,0),5)
cv2.imshow("Line",image)

#draw rectangle
# if you put thickness as -1 it fills the rectangle
image=np.zeros((512,512,3),np.uint8)
cv2.rectangle(image,(100,100),(300,250),(255,0,0),5)
cv2.imshow("rectangle",image)

#draw circle
image=np.zeros((512,512,3),np.uint8)
cv2.circle(image,(300,300),100,(0,250,0),3)
cv2.imshow("circle",image)

#draw any polygon using an array of points using numpy array
image=np.zeros((512,512,3),np.uint8)
#define points for polygon
pts=np.array([[10,50], [400,50], [90,200], [50,500]],np.int32)
#reshape the points in form required by polylines function
pts=pts.reshape((-1,1,2))
cv2.polylines(image,[pts],True,(0,0,255),0)
cv2.imshow("polygon",image)

#Add text
image=np.zeros((512,700,3),np.uint8)
cv2.putText(image,'Hi this is a example text',(150,150),cv2.FONT_HERSHEY_SIMPLEX,1,(250,250,0),0)
cv2.imshow("TEXT",image)

cv2.waitKey()
cv2.destroyAllWindows()