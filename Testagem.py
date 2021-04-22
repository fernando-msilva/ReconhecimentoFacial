from storage.Importar_imagens import importar
documento_id, id = importar("H_F_T","F_S_H",1,"Harry Potter","fugitivo procurado por Lord Voldemort")


import Recortar_faces
#Recortar_faces.recortar_faces(id=1,largura=150,path="H_F_T",path2="H_F_T_R",nome="Harry")
Recortar_faces.recortar_faces(id=id, documento_id=documento_id,largura=150)

import Treinamento
ids,faces = Treinamento.getImageById(id=id, documento_id=documento_id)
Treinamento.efmt(ids=ids,faces=faces)

import Reconhecer
#Reconhecer.reconhecedor_eigen(path3="H_F_T_R",id=1)
#Reconhecer.reconhecedor_eigen(path3="F_S_H",id=1)
Reconhecer.reconhecedor_eigen(id=id, documento_id=documento_id)
#Reconhecer.reconhecedor_eigen(path3="F_C_H_R",id=1)



