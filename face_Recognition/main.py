#written by V JAYASURYA ON 15-11-2022

import cv2

img=cv2.imread("Jayasurya.jpg")  # reading an image using imread() method of OpenCV

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # creating a object for haarcascadefrontal_face using Cascade Classifier method


grey_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # converting BGR image to GreyScale for high Accuracy

faces=face_cascade.detectMultiScale(grey_image,
scaleFactor=1.05,
minNeighbors=5)   #detecting face in the image read using detectMultiScale() method which outpus a array of coordinates wistha and height

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,200,0),5) #drawing a rectangle with the coordinates 


cv2.imshow("Detected Image",img) #showing the image in a window 

cv2.waitKey(0) #closing the window by pressing any key on keyboard

cv2.destroyAllWindows() #destroying all the windows 


