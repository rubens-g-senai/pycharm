import csv

simbolos = []
with open('elementos.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq, delimiter=',')
    for indice, linha in enumerate(leitor):
        if indice == 0:
            pass
        else:
            simbolos.append(linha[2])
    print(simbolos)

# Adicionar mais conteúdo ao arquivo elementos.csv (escrever no arquivo):
# with open('elementos.csv', mode='a', encoding='utf-8', newline='') as arq:
#     escritor = csv.writer(arq, delimiter=',')
#     escritor.writerow(['7','Nitrogênio','N','15'])
#     escritor.writerow(['8','Oxigênio','O','16'])
#     escritor.writerow(['9','Flúor','F','17'])