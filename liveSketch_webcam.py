import cv2
import numpy as np 

#function to generate sketch image
def sketch(image):
    #convert to grayscale
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #clean up using gaussian Blur
    img_blur=cv2.GaussianBlur(image,(5,5),0)

    #Extract edges using canny
    canny_img=cv2.Canny(image,10,70)

    #invert binary image
    ret, mask=cv2.threshold(canny_img,70,255,cv2.THRESH_BINARY_INV)

    return mask

# start video feed using cv2.VideoCapture()
# it returns frames i.e images and also
# ret is a boolean to check it reads a the frames
cap=cv2.VideoCapture(0)

while True:
    ret, frame =cap.read()
    cv2.imshow("Live Sketch",sketch(frame))
    if cv2.waitKey(1)==32: #32 is space bar
        break

# release camera
cap.release()
cv2.destroyAllWindows()

