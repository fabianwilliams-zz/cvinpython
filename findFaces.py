import cv2

counter = 0
img = cv2.imread("resc/WhatIsYouDoHere.png")
faceCascade = cv2.CascadeClassifier("resc/haarcascade_frontalface_default.xml")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
    cv2.putText(img,"Face Detected", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2)
    imgFaceOnly = img[y:y+h, x:x+w]
    cv2.imshow("Region of Interest"+str(counter), imgFaceOnly)
    cv2.imwrite("SavedFiles/FaceNumber_"+str(counter)+".jpg", imgFaceOnly)
    counter += 1

cv2.imshow("Original Image Marked", img)
cv2.waitKey(0)
