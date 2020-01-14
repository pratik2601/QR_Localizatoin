import cv2
font = cv2.FONT_HERSHEY_SIMPLEX

QR_cascade=cv2.CascadeClassifier('QRcascade.xml')
image=cv2.imread('QRmatrix2.png')

dimensions=image.shape
print("dimensions=",dimensions)
faces= QR_cascade.detectMultiScale(image,2,1,1,(100,100),(200,200))
ObjectNum=1
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.putText(image, "QR tag "+str(ObjectNum), (x, y), font, 0.8, (0, 0, 255), 2)
    ObjectNum += 1
    cv2.imshow('VideoFeed', image)
    #print('QR detected')

#cv2.imshow('VideoFeed2', image)
cv2.waitKey(0)
print("run successful")

cv2.destroyAllWindows()