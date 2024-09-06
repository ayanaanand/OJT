import cv2
import numpy as np

# Read the image with the OpenCV library
image = cv2.imread('test.jpg')

# Check if the image was successfully loaded
if image is None:
    print("Could not read the image")
    exit()

# Display the image
# cv2.imshow('Original Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#convert to greyscale
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#we apply a Gaussain blur into the above image
blurred_image = cv2.GaussianBlur(grey_image,(5,5),0)

#edge detection
edges = cv2.Canny(blurred_image,50,150)

#orginal image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

cv2.imshow('greyscale image', grey_image)
cv2.waitKey(0)

cv2.imshow('blurred image', blurred_image)
cv2.waitKey(0)

cv2.imshow('edges', edges)
cv2.waitKey(0)

cv2.destroyAllWindows()
