from storage.Conexao import conexao
from bson.objectid import ObjectId

from glob import glob
import shutil
import os
from cv2 import imwrite

PATH = os.path.dirname(os.path.abspath(__file__))


def importar(path_original, path_teste, id, nome, descricao):
    ''' 
        Função para adicionar novas imagens

        Descrição: Esta função deve ser usada para inserir novas imagens no componente de storage.
                   A inserção de imagens neste componente requer que sejam adicionados os metadados
                   relativos as novas imagens. esta função irá adicionar as imagens no sistema de arquivos
                   e criar o documento no mongodb com os metadados informados.

        Parâmetros:
            - path_teste: Endereço da pasta de imagens de teste
            - path_original: Endereço da pasta de imagens sem modificações
            - id: identificador único do indivíduo
            - nome: Nome do indivíduo presente nas imagens
            - descricao: Comentário relativo as características da base de dados
    '''

    imagens_teste = glob(f"{path_teste}/*")
    imagens_original = glob(f"{path_original}/*")

    if not os.path.exists(f"{PATH}/imagens/{id}/teste"):
        os.makedirs(f"{PATH}/imagens/{id}/teste")

    if not os.path.exists(f"{PATH}/imagens/{id}/original"):
        os.makedirs(f"{PATH}/imagens/{id}/original")
    
    for i in imagens_teste:
        shutil.copy(i,f"{PATH}/imagens/{id}/teste")

    for i in imagens_original:
        shutil.copy(i,f"{PATH}/imagens/{id}/original")

    metadados = {
        "imagens": {
            "teste": glob(f"{PATH}/imagens/{id}/teste/*"),
            "original": glob(f"{PATH}/imagens/{id}/original/*"),
            "treino": []
        },
        "id": id,
        "nome": nome,
        "descricao": descricao
    }
    
    con = conexao()

    id_documento = con.imagens.insert_one(metadados).inserted_id
    print(f"novo documento adicionado")
    return id_documento, id


def adicionar_imagens(id, id_documento, arquivo,nome,tipo):
    if not os.path.exists(f"{PATH}/imagens/{id}/treino"):
        os.makedirs(f"{PATH}/imagens/{id}/treino")

    try:
        imwrite(f"{PATH}/imagens/{id}/treino/{nome}",arquivo)
        con = conexao()
        #fugitivo_metadados = con.imagens.find_one({"id":1})
        #if tipo not in fugitivo_metadados["imagens"].keys():
        #    fugitivo_metadados["imagens"][tipo] = []
        #fugitivo_metadados["imagens"][tipo].append(f"{PATH}/imagens/{id}/treino/{nome}")
        con.imagens.update(
            {"_id": ObjectId(id_documento)},
            {"$push": {"imagens.$.treino":f"{PATH}/imagens/{id}/treino/{nome}","$position:0"}}
        )
    except Exception as e:
        print(e)