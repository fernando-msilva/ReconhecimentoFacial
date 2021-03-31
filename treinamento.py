import cv2
import os
import numpy as np


eigenface = cv2.face.EigenFaceRecognizer_create(num_components=10)
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()


def getImageById():
    paths = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    #print(paths)
    faces = []
    ids = []
    for pathImage in paths:
        faceImage = cv2.cvtColor(cv2.imread(pathImage), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(pathImage)[-1].split('.')[1])
        #print(id)
        ids.append(id)
        faces.append(faceImage)
        #cv2.imshow("Face", faceImage)
        #cv2.waitKey(10)
    return np.array(ids), faces

ids,faces = getImageById()
#print(ids)
#print(faces)

#Treinamento
print('Treinamento Iniciando')
eigenface.train(faces, ids)
eigenface.write('EigenClassifier.yml')

fisherface.train(faces, ids)
fisherface.write('FisherClassifier.yml')

lbph.train(faces, ids)
lbph.write('LbphClassifier.yml')
print('Treinamento Finalizado')

