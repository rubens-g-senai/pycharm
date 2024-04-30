# Simples, Composto, Encadeado

n1 = n2 = 0.0
media = 0.0
faltas = 0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
faltas = int(input('Digite a quantidade de faltas: '))

# Calcular a média aritmédica das notas
media = (n1 + n2) / 2

if (faltas >=10):
    print('Aluno reprovado por faltas')
elif (media >= 7): # Simples
    print("Resultado: Aprovado")
    print("Parabéns")
elif (media >= 5): # Encadeado
    print("Resultado: Você está de Recuperação")
else: # Composto
    print("Resultado: Reprovado")

print('Sua média é {}'.format(media))