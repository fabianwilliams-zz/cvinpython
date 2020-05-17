import cv2

### if you replace the ID of the camara as below the default is zero with a
### file path, it will play a video you have on file

myWebCam = cv2.VideoCapture(0)

### the below sets the size of the window and brightness
myWebCam.set(3,640)
myWebCam.set(4,480)
myWebCam.set(10,100)

while True:
    success, img = myWebCam.read()
    cv2.imshow("WebCam Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break