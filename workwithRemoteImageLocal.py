import cv2
import urllib3
import numpy as np

print("Computer Vision Verion is: " + cv2.__version__)

# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    image = np.asarray(bytearray(r.data), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image

# download the image URL and display it
url = "https://affoodie73427.blob.core.windows.net/photos/FabianW.png"
print("downloading %s" % (url))
imageOriginal = url_to_image(url)

# define a kernel for when we need image matrix
imgKernel = np.ones((7,7),np.uint8)
print(imgKernel)

# GrayScale
imageGray = cv2.cvtColor(imageOriginal,cv2.COLOR_BGR2GRAY)

#Gaussian Blur
imgBlur = cv2.GaussianBlur(imageGray,(9,9),0)

#Canny Edge Detector
imgCanny = cv2.Canny(imageGray,100,100)

#Image Dialation
imgDialate = cv2.dilate(imgCanny,imgKernel, iterations=1)

#Image Erosion
imgEroded = cv2.erode(imgDialate,imgKernel, iterations=1)



cv2.imshow('Image Greyscale', imageGray)
cv2.imshow('Image Gaussian Blur', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dialated Image', imgDialate)
cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)