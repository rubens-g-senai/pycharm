# Manipulação de arquivos de texto.

# print(f'\nMétodo read():\n')
# print(manipulador.read())

# print(f'\nMétodo readline():\n')
# print(manipulador.readline())
# print(manipulador.readline())

# print(f'\nMétodo readlines():\n')
# print(manipulador.readlines())
texto = input('Qual termo deseja procurar no arquivo? ')
try:
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()
        if texto in linha:
            print(f'A string foi encontrada!')
            print(linha)
        #else:
            #print(f'String não encontrada!')
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()

# Escrever em arquivos de texto
# texto = '\nPython é usado em Ciência de Dados extensivamente'
# try:
#    manipulador = open('arquivo.txt', 'a', encoding='utf-8')
#    manipulador.write(texto)
# except IOError:
#    print(f'Não foi possível abrir o arquivo')
# else:
#    manipulador.close()

#frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola']

# Criar e gravar o arquivo
#try:
#    manipulador = open('frutas.dat', 'w', encoding='utf-8')
#    manipulador.writelines(frutas)
# except IOError:
#    print(f'Não foi possível abrir o arquivo')
# else:
#    manipulador.close()

# # Ler o arquivo criado:
# try:
#    manipulador = open('frutas.dat', 'r', encoding='utf-8')
#    print(manipulador.read())
# except IOError:
#    print(f'Não foi possível abrir o arquivo')
# else:
#    manipulador.close()

# Com gerenciador de contexto e palavra-chave with:
#with open('frutas.dat', 'r', encoding='utf-8') as a:
#   for linha in a:
#      print(linha, end='')