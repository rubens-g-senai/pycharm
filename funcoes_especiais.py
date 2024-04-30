# Funções lambda (anônimas)
# Sintaxe
# lambda argumentos: expressão

# quadrado = lambda x: x**2

# for i in range(1,11):
#     print(quadrado(i))

# par = lambda x: x %2 == 0 # verifica se o número é par (True ou False)
# print(par(8))

# f_c = lambda f: (f - 32) * 5/9 # função que converte temperatura de fahrenheit para celsius
# print(f_c(80)) # 80 F° = 26.66 C°

# Função map()
# Sintaxe
# map(função, interável)

# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

# palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)

# Função filter()
# Sintaxe:
# filter(função, sequência)

# def numeros_pares(n):
#     return n % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# num_par = list(filter(numeros_pares, numeros))
# print(num_par)

# num_impar = list(filter(lambda x: x % 2 != 0, numeros)) 
# print(num_impar) # mostra os números impares da lista

# Função reduce()
# Sintaxe
# reduce(função, sequência, valor_inicial)

from functools import reduce

# def mult(x, y):
#     return x * y

# numeros = [1,2,3,4,5]

# total = reduce(mult, numeros)
# print(total)

# Soma cumulativa dos quadrados de valores, usando expressão lambda

numeros = [1,2,3,4]
# ((1² + 2²)² + 3²)² + 4²

total = reduce(lambda x, y: x**2 + y**2, numeros)
print(total)