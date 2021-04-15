from storage.Conexao import conexao
from bson.objectid import ObjectId

import os
from cv2 import imread

def recuperar(documento_id,tipo):
    """
        Função para retornar um set de imagens de treino ou teste.

        Parâmetros:
            - id: Identificador do indivíduo a ser recuperado
            - tipo: Tipo de imagem a ser recuperada (teste ou treino)
    """

    con = conexao()

    fugitivo_metadados = con.imagens.find_one({"_id":ObjectId(documento_id)})

    fugitivo_imagens = fugitivo_metadados["imagens"][tipo]

    imagens_recuperadas = []

    """
    for imagem in fugitivo_imagens:
        with open(imagem,"rb") as img:
            imagens_recuperadas.append([
                os.path.basename(img.name),
                img.read()
            ])
    

    """
    for imagem in fugitivo_imagens:
        with open(imagem,"rb") as img:
            imagens_recuperadas.append([
                os.path.basename(img.name),
                imread(img.name)
            ])
    
    return fugitivo_metadados["nome"], imagens_recuperadas