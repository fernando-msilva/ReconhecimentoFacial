import cv2
import os
import numpy as np
from statistics import mean

recognizer = cv2.face.EigenFaceRecognizer_create(num_components=36)
detector_faces_01 = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  # Treinamento da Detecção de faces

def reconhecedor_eigen(path3,id):
    recognizer.read(f'EigenClassifier_ID{id}.yml')
    trust_list = []
    width, height = 150, 150
    font = cv2.FONT_HERSHEY_COMPLEX
    n = 0

    paths = [os.path.join(path3, f) for f in os.listdir(path3)]
    for pathImage in paths:
        imagem = cv2.imread(pathImage)  # abre a imagem
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # Converte a imagem em escala de cinza
        faces_detectadas = detector_faces_01.detectMultiScale(imagem_cinza, scaleFactor=1.2, minSize=(150, 150)) #Detecta faces dentro da foto
        for (x, y, w, h) in faces_detectadas:
            try:
                imagem_face = cv2.resize(imagem_cinza[y:y + h, x:x + w], (width, height))
                id, trust = recognizer.predict(imagem_face)
                if trust < 8000.0:
                    n = n + 1
                    cv2.rectangle(imagem_cinza, (x, y), (x + w, y + h), (255, 255, 255, 2))
                    cv2.putText(imagem_cinza, str(f"ID:{id}"), (x, y + (h + 65)), font, 3, (255, 255, 255), 2)
                    cv2.putText(imagem_cinza, str(f"trust:{trust}"), (x, y + (h - 60)), font, 2, (255, 255, 255), 2)
                    cv2.imshow("Face", imagem_cinza)
                    cv2.waitKey(2000)
                    trust_list.append([pathImage, trust])
                else:
                    continue
            except Exception as e:
                print(e)
    print(f"Foram detectadas {n} faces em {len(paths)} imagems")
    print(trust_list)


