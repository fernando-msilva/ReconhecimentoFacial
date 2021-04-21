import cv2
import os
import numpy as np
from statistics import mean

recognizer = cv2.face.EigenFaceRecognizer_create(num_components=36)
detector_faces_01 = cv2.CascadeClassifier("/opt/ml/haarcascade_frontalface_default.xml")  # Treinamento da Detecção de faces

def reconhecedor_eigen(imagem_bytes):
    recognizer.read('/opt/ml/EigenClassifier.yml')
    trust_list = []
    width, height = 150, 150
    font = cv2.FONT_HERSHEY_COMPLEX
    n = 0

    nparr = np.fromstring(imagem_bytes, np.uint8)
    imagem = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # Converte a imagem em escala de cinza
    faces_detectadas = detector_faces_01.detectMultiScale(imagem_cinza, scaleFactor=1.2, minSize=(150, 150)) #Detecta faces dentro da foto
    for (x, y, w, h) in faces_detectadas:
        try:
            imagem_face = cv2.resize(imagem_cinza[y:y + h, x:x + w], (width, height))
            id, trust = recognizer.predict(imagem_face)
            if trust < 8000.0:
                n = n + 1
                trust_list.append(trust)
            else:
                continue
        except Exception as e:
            return e
    
    return trust_list


