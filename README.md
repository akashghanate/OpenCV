# OpenCV
Basics programs to learn OpenCV with some miniprojects
### pre-intallation required
* python2/ python3
* OpenCV2
* matplotlib
* numpy

***
### Basics programs are:
1. **readWriteDisplayImage.py** - code to read image into a varaible, displaying the stored image in a window and saving stored image in different formats, also to get the height-width parameters of the image.

2. **greyScaling.py** - code to convert RGB(colour image) into greyscale (B/W image).

3. **colorSpaces** - Color spaces are a way to represent the color channels present in the image that gives the image that particular hue. There are several different color spaces and each has its own significance.
Some of the popular color spaces are RGB (Red, Green, Blue), CMYK (Cyan, Magenta, Yellow, Black), HSV (Hue, Saturation, Value).
   1. BGR color space: OpenCV’s default color space is RGB. However, it actually stores color in the BGR format. It is an additive color model where the different intensities of Blue, Green and Red give different shades of color.
   2. HSV color space: It stores color information in a cylindrical representation of RGB color points. It attempts to depict the colors as perceived by the human eye. Hue value varies from 0-179, Saturation value varies from 0-255 and Value value varies from 0-255. It is mostly used for color segmentation purpose.<br>
This code is to get different colorspace values for a given pixel of the image.<br>

4. **histograms.py** - code for image analysis using Matplotlib.The image should be used in a PNG file as matplotlib supports only PNG images.

5. **splitRGBchannels.py** - Splitting an “RGB” image creates three new images each containing a copy of one of the original bands (red, green, blue).

6. **drawImageShapes.py** - code to draw shapes like line, circle, rectangle and also writing a text on a created black image. 

***
### Under Image Manipulation:
1. **arithmeticOper.py** 	
2. **bitwise_masking.py** 
3. **blurring.py** 	
4. **dilation_erosion.py**
5. **edgeDetection.py** 
6. **imagePyramid.py** 	
7. **rotation.py** 
8. **scaling_interpolation.py** 	
9. **sharpening.py** 
10. **thresholding.py** - thresholding that is converting image to binary form 	
11. **translation.py** - translation of images using warpAffine 	

### Under Image Segmentation:
1. **contours.py**
2. **sortingContours.py**
