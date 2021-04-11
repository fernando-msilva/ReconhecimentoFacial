import cv2
import os
import numpy as np
import time

from storage.Recuperar_imagens import recuperar

def getImageById(id):
    faces = []
    ids = []

    #paths = [os.path.join("./storage/imagens/1/treino", f) for f in os.listdir("./storage/imagens/1/treino")]

    nome, imagens = recuperar(id,"treino")

    for imagem_nome,imagem in imagens:
        imagem_face = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        id=int((imagem_nome.split("."))[1])
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
