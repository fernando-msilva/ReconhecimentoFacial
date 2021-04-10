import glob

def getImages(id):
    return glob.glob(f'fotos/pessoa.{id}*')