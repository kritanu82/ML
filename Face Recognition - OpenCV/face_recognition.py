import cv2
import numpy as np
import os 

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

recognizer = cv2.face.LBPHFaceRecognizer_create()

assure_path_exists("trainer/")

recognizer.read('trainer/trainer.yml')

cascadePath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

cam = cv2.VideoCapture(0)

while True:
    
    ret, face_recognition = cam.read()

    gray = cv2.cvtColor(face_recognition,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    for(x,y,w,h) in faces:

        cv2.rectangle(face_recognition, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        if(Id == 1):
            Id = "Kritanu {0:.2f}%".format(round(100 - confidence, 2))
        if(Id == 2):
            Id = "Dhrumil {0:.2f}%".format(round(100 - confidence, 2))
        if(Id == 3):
            Id = "Kritanu with specs {0:.2f}%".format(round(100 - confidence, 2))
        if(Id == 4):
            Id = "Param {0:.2f}%".format(round(100 - confidence, 2))

        cv2.rectangle(face_recognition, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(face_recognition, str(Id), (x,y-40), font, 1, (255,255,255), 3)

    cv2.imshow('face recognition',face_recognition) 

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()

cv2.destroyAllWindows()