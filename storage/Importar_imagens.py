from Conexao import conexao

def importar():
    ''' 
        Função para adicionar novas imagens

        Descrição: Esta função deve ser usada para inserir novas imagens no componente de storage.
                   A inserção de imagens neste componente requer que sejam adicionados os metadados
                   relativos as novas imagens. esta função irá adicionar as imagens no sistema de arquivos
                   e criar o documento no mongodb com os metadados informados.
        
    '''
    
    con = conexao()


if __name__ == "__main__":
    importar()