from pyzbar import pyzbar
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread("QRmatrix4.png")
imageDimension = image.shape
print(imageDimension)
barcodes = pyzbar.decode(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 10)

Localization_variable = ()
NumQRtags = 0
for barcode in barcodes:
    NumQRtags += 1
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    barcodeData = barcode.data.decode()
    barcodeType = barcode.type
    Location = (round((x + w) / 2), round((y + h) / 2))
    QRobject = Location + (int(barcodeData),)
    Localization_variable = Localization_variable + (QRobject,)
    #text = "{} ({})".format(barcodeData, barcodeType)
    text = "{} cm".format(barcodeData)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
Localization_variable = (NumQRtags,) + Localization_variable
print(Localization_variable)

Object_variable = ()
NumObjects = 0
for (x, y, w, h) in faces:
    NumObjects += 1
    Location = (round((x + w) / 2), round((y + h) / 2))
    Object_variable = Object_variable + (Location,)
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
    text = "Face"
    #cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


Object_variable = (NumObjects,) + Object_variable
print(Object_variable)

# calculating object distance assuming only two QR tags are in image
QR_left_location = Localization_variable[1][0]
QR_Right_location = Localization_variable[2][0]
QR_left_distance = Localization_variable[1][2]
QR_Right_distance = Localization_variable[2][2]
print(QR_left_distance)
print(QR_Right_distance)

for i in range(Object_variable[0]):
    Object_location = Object_variable[i + 1][0]
    Object_distance = ((Object_location - QR_Right_location) * (QR_left_distance - QR_Right_distance) / (
                QR_left_location - QR_Right_location)) + QR_Right_distance
    Object_distance=round(Object_distance,2)
    print(Object_distance)
    text=str(Object_distance)+ " cm"
    cv2.putText(image,text, (int(Object_variable[i+1][0]),int(Object_variable[i+1][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    print(str((Object_variable[i+1][0])))
    print(str((Object_variable[i + 1][1])))
# display image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
