import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)

while True:
    ref,img=cap.read()


    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray,1.1,10)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        cv2.imshow('VideoFeed', img)
        print('Face detected')

    if(cv2.waitKey(1)==27):
        break

cap.release()
cv2.destroyAllWindows()