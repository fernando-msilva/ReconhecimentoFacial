import cv2
import os
import numpy as np


def getImageById(path2):
    faces = []
    ids = []

    paths = [os.path.join(path2, f) for f in os.listdir(path2)]

    for pathImage in paths:
        imagem_face = cv2.cvtColor(cv2.imread(pathImage), cv2.COLOR_BGR2GRAY)
        id=int((pathImage.split("."))[1])
        ids.append(id)
        faces.append(imagem_face)
    print(f"Foram retornadas {len(ids)} faces do id:{ids[0]}")
    return ids, faces


def efmt(ids,faces):
    print("Treinamento iniciado")
    eigenface = cv2.face.EigenFaceRecognizer_create(num_components=80)
    eigenface.train(faces, np.array(ids))
    eigenface.write(f'EigenClassifier_ID{ids[0]}.yml')
    print("Modelo treinado com sucesso")
