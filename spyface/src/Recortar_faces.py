#pip install opencv-python
#pip install opncv-contrib-python

import cv2
import os
import numpy as np

from storage.Recuperar_imagens import recuperar
from storage.Importar_imagens import adicionar_imagens

#Criando o modelo que irá detectar as faces
detector_faces_01 = cv2.CascadeClassifier("/opt/config/haarcascade_frontalface_default.xml")



def recortar_faces(id, documento_id,largura):
    amostra = 1
    altura = largura

    #paths = [os.path.join(path, f) for f in os.listdir(path)]

    nome, imagens = recuperar(documento_id,"original")

    faces = []

    for imagem_nome, imagem in imagens:
        try:
            #imagem = cv2.imread(pathImage) #abre a imagem
            #nparr = np.fromstring(imagem_bytes, np.uint8)
            #imagem = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
            cv2.waitKey(10)  # Deixa ela aberta durante uma janela de tempo
            imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # Converte a imagem em escala de cinza
            faces_detectadas = detector_faces_01.detectMultiScale(imagem_cinza,scaleFactor=1.2,minSize=(150,150))
            for (x, y, l, a) in faces_detectadas:
                cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 255, 255), 2)  # Desenha o retangulo vermelho ao redor da face
                #cv2.imshow("Face", imagem_cinza)  # Mostra a imagem
                #cv2.waitKey(100)  # Deixa ela aberta durante uma janela de tempo
                # Salvar as imagens
                if np.var(imagem_cinza) > 10:
                    imagem_face = cv2.resize(imagem_cinza[y:y + a, x:x + l], (largura, altura))
                    #cv2.imshow("Face", imagem_face)  # Mostra a imagem
                    #cv2.waitKey(100)  # Deixa ela aberta durante uma janela de tempo
                    #cv2.imwrite(f"{path_destino}/{nome}" + "." + str(id) + "." + str(amostra) + ".jpg", imagem_face)
                    nome_arquivo = f"{nome}" + "." + str(id) + "." + str(amostra) + ".jpg"
                    adicionar_imagens(id,documento_id,imagem_face,nome_arquivo,"treino")
                    faces.append([imagem_face, nome_arquivo])
                    print(f"Foto {amostra} recortada com sucesso")
                    amostra += 1
        except Exception as e:
            print(e)

    #adicionar_imagens(id,documento_id,faces,"treino")
    print(f"Foram recortadas {amostra - 1} faces de {len(imagens)} imagens")
