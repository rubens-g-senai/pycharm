import random
import os

# print('Gerar cinco números aleatórios entre 1 e 50: \n')
# for i in range(5): # laço de repetição
#     n = random.randint(1,50) #(limite inferior, limite superior)
#     print(f'Número gerado: {n}')

# valor = random.random() # random = aleatório
# print(f'Número gerado: {round(valor * 10, 2)}')
#
# valor = random.uniform(1,100)
# print(f'Número: {round(valor, 4)}') # flutuante = float
#
L = [2,4,6,9,10,13,14,16,18,20,21,27,33]
n = random.choice(L) # choice = escolha
print(f'Número escolhido: {n}')
#
# n = random.sample(L,3) # sample = amostra
# print(f'Números escolhidos: {n}')
#
# Embaralhar
# os.system('cls')
# print(f'Exibir a lista original: {L}')
# print(f'Embaralhar a lista e exibi-la:')
# n = random.shuffle(L) # suffle = embaralhar
# print(L)

