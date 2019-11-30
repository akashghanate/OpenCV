import cv2
import numpy as np 

image=cv2.imread('/home/akashkg/test_imgs/img12.png')
cv2.imshow("original",image)
cv2.waitKey()
copy=image
#crate a blank image as same dimensions as original image
blank=np.zeros(image.shape)
#grayscale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#find edges
canny=cv2.Canny(gray,50,200)
cv2.imshow("canny edges",canny)
cv2.waitKey()
#find and draw contours
ret,contours, hierarchy=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(blank,contours,-1,(0,255,0),2)
cv2.imshow("contours",blank)
cv2.waitKey()

# ----------------------actual sorting code by area ------------------------------------------------------

#function use to display contour area
def get_contour_area(contours):
    #returns the areas as list
    all_areas=[]
    for cnt in contours:
        area=cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

#areas before sorting
print("contour areas before soring")
print(get_contour_area(contours))

#sort contours large to small
sorted_contours=sorted(contours,key=cv2.contourArea,reverse=True)
print("contour areas after soring")
print(get_contour_area(sorted_contours))

#iterate over contours and draw one at a time
for c in sorted_contours:
    cv2.drawContours(image,[c],-1,(255,0,0),3)
    cv2.waitKey()
    cv2.imshow("Original image",image)

cv2.waitKey()
cv2.destroyAllWindows()