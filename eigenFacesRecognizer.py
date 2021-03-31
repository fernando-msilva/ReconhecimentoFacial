import cv2

faceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.read("EigenClassifier.yml")
width, height = 220,220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

camera = cv2.VideoCapture(0)

while True:
    connected, image = camera.read()
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detectedFaces = faceDetector.detectMultiScale(grayImage, scaleFactor=1.5, minSize=(30,30))

    for(x, y, w, h) in detectedFaces:
        faceImage = cv2.resize(grayImage[y:y + h, x:x + w], (width, height))
        cv2.rectangle(image, (x,y), (x + w, y+ h), (0,0,255, 2))
        id, trust = recognizer.predict(faceImage)
        cv2.putText(image, str(id), (x,y+ (h + 30)), font, 2, (0,0,255))

    cv2.imshow("Face", image)
    if cv2.waitKey(1) == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()