import Recortar_faces
#Recortar_faces.recortar_faces(id=1,largura=150,path="H_F_T",path2="H_F_T_R",nome="Harry")
Recortar_faces.recortar_faces(id=1,largura=150,path_destino="H_F_T_R_2")

import Treinamento
ids,faces = Treinamento.getImageById(path2="H_F_T_R_2")
Treinamento.efmt(ids=ids,faces=faces)

import Reconhecer
#Reconhecer.reconhecedor_eigen(path3="H_F_T_R",id=1)
#Reconhecer.reconhecedor_eigen(path3="F_S_H",id=1)
Reconhecer.reconhecedor_eigen(id=1)
#Reconhecer.reconhecedor_eigen(path3="F_C_H_R",id=1)





