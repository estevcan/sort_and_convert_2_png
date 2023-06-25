import os
import re
import shutil

# Diretório contendo os arquivos JPEG
diretorio = 'C:/Users/Weback/Documents/estevan/centelha/landing_page'

# Expressão regular para extrair o número dos arquivos
padrao_numero = re.compile(r'\d+')

# Lista de arquivos JPEG no diretório
arquivos_jpeg = [arquivo for arquivo in os.listdir(diretorio) if arquivo.lower().endswith('.jpeg')]

# Função para extrair o número do nome do arquivo
def extrair_numero(nome_arquivo):
    numero = padrao_numero.search(nome_arquivo)
    return int(numero.group()) if numero else -1

# Ordenar arquivos com base nos números extraídos
arquivos_jpeg_ordenados = sorted(arquivos_jpeg, key=lambda x: extrair_numero(x))

# Diretório de destino para os arquivos ordenados
diretorio_destino = 'C:/Users/Weback/Documents/estevan/centelha/landing_page_sort'

# Mover arquivos para o diretório de destino, mantendo a ordem
for i, arquivo in enumerate(arquivos_jpeg_ordenados):
    shutil.move(os.path.join(diretorio, arquivo), os.path.join(diretorio_destino, f'{i+1}.jpeg'))
