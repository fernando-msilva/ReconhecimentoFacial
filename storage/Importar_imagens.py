from storage.Conexao import conexao

from glob import glob
import shutil
import os

PATH = os.path.dirname(os.path.abspath(__file__))


def importar(path_teste, path_treino, id, nome, descricao):
    ''' 
        Função para adicionar novas imagens

        Descrição: Esta função deve ser usada para inserir novas imagens no componente de storage.
                   A inserção de imagens neste componente requer que sejam adicionados os metadados
                   relativos as novas imagens. esta função irá adicionar as imagens no sistema de arquivos
                   e criar o documento no mongodb com os metadados informados.

        Parâmetros:
            - path_teste: Endereço da pasta de imagens de teste
            - path_treino: Endereço da pasta de imagens de treino
            - id: identificador único do indivíduo
            - nome: Nome do indivíduo presente nas imagens
            - descricao: Comentário relativo as características da base de dados
    '''

    imagens_teste = glob(f"{path_teste}/*")
    imagens_treino = glob(f"{path_treino}/*")

    if not os.path.exists(f"{PATH}/imagens/{id}/teste"):
        os.makedirs(f"{PATH}/imagens/{id}/teste")

    if not os.path.exists(f"{PATH}/imagens/{id}/treino"):
        os.makedirs(f"{PATH}/imagens/{id}/treino")
    
    for i in imagens_teste:
        shutil.copy(i,f"{PATH}/imagens/{id}/teste")

    for i in imagens_treino:
        shutil.copy(i,f"{PATH}/imagens/{id}/treino")

    metadados = {
        "imagens_teste": glob(f"{PATH}/imagens/{id}/teste/*"),
        "imagens_treino": glob(f"{PATH}/imagens/{id}/treino/*"),
        "id": id,
        "nome": nome,
        "descricao": descricao
    }
    
    con = conexao()

    print(f"novo documento com id {con.imagens.insert_one(metadados).inserted_id}")