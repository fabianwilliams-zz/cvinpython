import cv2

### read local image
fabheadimg = cv2.imread("resc/fabianheadshotprof.png")

#get (shape) size of image
print(fabheadimg.shape)

# resize image providing Width then Height
fabheadimg_408by412 = cv2.resize(fabheadimg,(408,412))
print(fabheadimg_408by412.shape)

# Crop Image providing Height then Width. Not using Cv2 here!
imgCroppped = fabheadimg[10:600,150:650]

cv2.imshow("Fabian HeadShot Output", fabheadimg)
cv2.imshow("Fabian HeadShot 408by412", fabheadimg_408by412)
cv2.imshow("Cropped HeadShot", imgCroppped)
cv2.waitKey(0)
