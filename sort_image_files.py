import os
from PIL import Image

# lista todos os arquivos do diretório
path_a = '../dataset/5dataset_balanced_raw'
path_b = '.'

files_a = os.listdir(path_a)

# ordena os arquivos em ordem alfabética
files_a.sort()

# percorre cada arquivo
for i, file in enumerate(files_a):

    # verifica se o arquivo é uma imagem
    #if file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.JPEG')):

    # abre a imagem
    img = Image.open(os.path.join(path, file))
    # renomeia o arquivo com o índice (começando de 1) e extensão png
    new_name = f'{i+1}.png'
    # salva a imagem com o novo nome
    img.save(new_name)

files_b = os.listdir(path_b)

files_b.sort()

for i, file in enumerate(files_b):
    print(file)
