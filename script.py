import os
import shutil

print('Esse script irá clonar o arquivo indicado quantas vezes você desejar e informar onde encontrá-los')

file_path = input('Informe a localização do arquivo: (ex.: C:/nome-do-arquivo.txt ou /pasta/nome-do-arquivo): ')

number_of_clones = int(input('Informe quantas vezes deseja clonar esse arquivo: '))

file_name, file_extension = os.path.splitext(file_path)

path_to_copies = file_name + '-copies'
if not os.path.exists(path_to_copies):
    os.makedirs(path_to_copies)

for x in range(number_of_clones):
    shutil.copyfile(file_path, path_to_copies + '/copy-' + str(x) + file_extension)

print('Os arquivos foram duplicados em ' + path_to_copies)