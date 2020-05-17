import cv2
print("Computer Vision Verion is: " + cv2.__version__)
### read local image
fabheadimg = cv2.imread("resc/fabianheadshotprof.png")
cv2.imshow("Fabian HeadShot Output", fabheadimg)
cv2.waitKey(0)
