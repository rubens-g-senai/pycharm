# Lista: representa uma sequência de valores

# Sintaxe: nome_lista = [valores]

n1 = [4,6,7,8,0,3]
n2 = [1,6,3,0,12,11]
valores = n1 + n2
valores[0] = 9
print(len(valores)) # len = comprimento ( neste caso, len está informando a quantidade de elementos dentro das duas listas )
# print(sorted(valores, reverse=True)) # sorted = informa a versão ordenada das listas do menor ao maior e reverse = True ordena ao contrário
# print(sum(valores)) # sum = soma de todos os valores
# print(min(valores)) # min = valor mínimo da lista
# print(max(valores)) # max = valor máximo da lista

# valores.append(13) # append = acrescenta um número na lista
# print(valores)
# valores.pop() # pop = retira um valor da lista - () vazio retira o último número da lista
# print(valores)
# valores.pop(3)
# print(valores)
# valores.insert(3,21) # insert = insere na posição definida um número na lista (posição, número)
# print(valores)
# print(17 in valores) # in = pergunta se tem um número informado na lista

# planetas = ['Mercúrio', 'Vênus','Marte','Saturno','Urano','Netuno']
# for planeta in planetas:
#     print(planeta)

bebidas = []
#
for i in range(5):
     # print(f'Digite primeira bebida favorita:')
     # bebida = input()
     # print(f'Digite segunda bebida favorita:')
     # bebida = input()
     # print(f'Digite terceira bebida favorita:')
     # bebida = input()
     # print(f'Digite quarta bebida favorita:')
     # bebida = input()
     print(f'Digite até 5 bebidas favoritas! Bebida {i+1}:')
     bebida = input()
     bebidas.append(bebida)
#
bebidas.sort() # classifica e ordena em ordem alfabética
#
print(f'\nBebidas escolhidas em ordem alfabética:')
for bebida in bebidas:
    print(bebida)
#
print(f'\nSaúde!')