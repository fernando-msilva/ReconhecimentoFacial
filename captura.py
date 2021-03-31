import cv2
import numpy as np

classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  # Treinamento da Detecção de faces
classificadorOlhos = cv2.CascadeClassifier("haarcascade_eye_default.xml")  # Treinamento da Detecção de faces
camera = cv2.VideoCapture(0)  # Captura imagem da camera

# Teste para captura das fotos de treinamento
# Formato: Pessoa.{id}.{numeroFoto}.jpg
amostra = 1
numeroAmostras = 25
id = input('Digite seu Identificador')
largura, altura = 220,220  # Controla o tamanho das imagens, pois os metodos necessitam que as imagens tenham o mesmo tamanho
print("Capturando as faces")

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # Converte a imagem em escala de cinza
    # print(np.average(imagemCinza))
    facesDetectadas = classificador.detectMultiScale(imagemCinza,
                                                     scaleFactor=1.5,  # Escala da Imagem
                                                     minSize=(150, 150))

    for(x,y,l,a) in facesDetectadas:
        cv2.rectangle(imagem,(x,y),(x+l, y+ a),(0,0,255),2) # Desenha o retangulo vermelho ao redor da face
        #regiao = imagem[y:y+a, x:x + l]
        #regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        #olhosDetectados = classificadorOlhos.detectMultiScale(regiaoCinzaOlho)
        #for(ox, oy, ol, oa) in olhosDetectados:
        #    cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0,255,0),2)
        # Salvar as imagens que estão sendo capturadas pela WebCan
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            if np.average(imagemCinza) > 110:
                imagemFace = cv2.resize(imagemCinza[y:y + a, x:x+ l], (largura, altura))
                cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
                print("[foto " + str(amostra) + "capturada com sucesso]")
                amostra +=1;

    cv2.imshow("Face", imagem)
    #cv2.waitKey(1)
    if(amostra >= numeroAmostras + 1):
        break

print("Faces capturadas com sucesso")
camera.release()
cv2.destroyAllWindows()
