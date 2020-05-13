#histogram bacially is a bar graph 
import cv2
import numpy as np 

#use matplotlib to create histogram plots
from matplotlib import pyplot as plt 
#The image should be used in a PNG file as matplotlib supports only PNG images.
image=cv2.imread('/home/akashkg/OpenCV/images/shapes.png')

#calculating histogram using calcHist
# cv2.calcHist([images],[channels],mask,[histSize],ranges[,])
histogram=cv2.calcHist([image],[0],None,[256],[0,256])

#ploting histogram, ravel() flatens our image array
plt.hist(image.ravel(),256,[0,256]); plt.show()

#viewing separate color channels
color=('b','g','r')

#separate color and plot each in histogram
for i,col in enumerate(color):
    histogram2=cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2,color=col)
    plt.xlim([0,256])
plt.show()