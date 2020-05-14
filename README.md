# OpenCV
Basics programs to learn OpenCV using python with some miniprojects
### pre-intallations required
* python2/ python3
* OpenCV2
* matplotlib
* numpy

***
### Basic programs are:
1. **readWriteDisplayImage.py** - code to read image into a varaible, displaying the stored image in a window and saving stored image in different formats(JPEG, PNG), also to get the height-width parameters of the image.

2. **greyScaling.py** - code to convert RGB(colour image) into greyscale (B/W image).

3. **colorSpaces** - Color spaces are a way to represent the color channels present in the image that gives the image that particular hue. There are several different color spaces and each has its own significance.
Some of the popular color spaces are RGB (Red, Green, Blue), CMYK (Cyan, Magenta, Yellow, Black), HSV (Hue, Saturation, Value).
   1. BGR color space: OpenCV’s default color space is RGB. However, it actually stores color in the BGR format. It is an additive color model where the different intensities of Blue, Green and Red give different shades of color.
   2. HSV color space: It stores color information in a cylindrical representation of RGB color points. It attempts to depict the colors as perceived by the human eye. Hue value varies from 0-179, Saturation value varies from 0-255 and Value value varies from 0-255. It is mostly used for color segmentation purpose.<br>
This code is to get different colorspace values for a given pixel of the image.<br>

4. **histograms.py** - code for image analysis using Matplotlib. The image should be used in a PNG file as matplotlib supports only PNG images.

5. **splitRGBchannels.py** - Splitting an “RGB” image creates three new images each containing a copy of one of the original bands (red, green, blue).

6. **drawImageShapes.py** - code to draw shapes like line, circle, rectangle and also writing a text on a created black image. 

***
### Under Image Manipulation:
1. **arithmeticOper.py** - Operations as add and subtract are used to vary the intensties of color in the image ( brightness)

2. **bitwise_masking.py** - Bitwise operations are used for extracting essential parts in the image.Also, Bitwise operations helps in image masking. Image creation can be enabled with the help of these operations. These operations can be helpful in enhancing the properties of the input images. <br>
**NOTE:** The Bitwise operations should be applied on input images of same dimensions.

3. **blurring.py** - Image Blurring refers to making the image less clear or distinct. It is done with the help of various low pass filter kernels.<br>
 **Advantages of blurring:**
    1. It helps in Noise removal. As noise is considered as high pass signal so by the application of low pass filter kernel we restrict noise.
    2. It helps in smoothing the image.
    3. Low intensity edges are removed.
    4 .It helps in hiding the details when necessary. For e.g. in many cases police deliberately want to hide the face of the victim, in such cases blurring is required.<br>
The code has different types of blurring- box blur, Gaussian blur, Medium blur, Bilateral blur.

4. **dilation_erosion.py** - Morphological operations are a set of operations that process images based on shapes. They apply a structuring element to an input image and generate an output image.The most basic morphological operations are two: Erosion and Dilation.<br>
Basics of Erosion: Erodes away the boundaries of foreground object, Used to diminish the features of an image.<br>
Basics of dilation: Increases the object area, Used to accentuate features.<br>

5. **edgeDetection.py** - Edge detection includes a variety of mathematical methods that aim at identifying points in a digital image at which the image brightness changes sharply or, more formally, has discontinuities. The points at which image brightness changes sharply are typically organized into a set of curved line segments termed edges. One of the best methods in canny edge detection

6. **imagePyramid.py** - Image Pyramids are one of the most beautiful concept of image processing.Normally, we work with images with default resolution but many times we need to change the resolution (lower it) or resize the original image in that case image pyramids comes handy. The pyrUp() function increases the size to double of its original size and pyrDown() function decreases the size to half.

7. **rotation.py** - cv2 offer rotation and scaling by using the function- cv2.getRotationMatrix2D(rotation_centre_x, rotation_centre_y, rotation_angle, scale).

8. **scaling_interpolation.py** - Different shrinking(downsampling) and zooming(upsampling) methods.	

9. **sharpening.py** - it's opposite to blurring, it strengthens the edges.

10. **thresholding.py** - Thresholding is a technique in OpenCV, which is the assignment of pixel values in relation to the threshold value provided. In thresholding, each pixel value is compared with the threshold value. If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value (generally 255). Thresholding is a very popular segmentation technique, used for separating an object considered as a foreground from its background.  <br>
**NOTE:** image is first converted to grayscale before thresholding


11. **translation.py** - translation of images using warpAffine function i.e moving the frame coorfinates in the window. 	

***

### Under Image Segmentation:

1. **contours.py** - segmentation is partitioning images into different regions, contours are the continuous lines or curves that bound/cover the object completely, contours are important in object dtetection and shape analysis
 
2. **sortingContours.py**
