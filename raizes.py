import sys
import os

def raizes(a, b, c):
    d = (b**2 - 4*a*c)
    x1 = (-b + d**(1/2)) / (2*a)
    x2 = (-b - d**(1/2)) / (2*a)

    print(f'\nValor de x1: {x1:.2f}')
    print(f'Valor de x2: {x2:.2f}\n')

    # Opcional: retornar os valores em uma lista
    valores = []
    valores.append(x1)
    valores.append(x2)

    return valores

if __name__=='__main__':
    while True:
        print(f'Calcular as raízes de uma equação de 2º grau\n')
        print(f'Equação no formato ax² + bx + c = 0\n')

        try:
            a = float(input('Entre com o valor de a: '))
            b = float(input('Entre com o valor de b: '))
            c = float(input('Entre com o valor de c: '))
        except ValueError:
            print(f'Digite somente números!')
        else:
            res = raizes(a,b,c)
            print(res)

        while True:
            continua = input('\nDigite q para sair ou n para novo cálculo: ')
            if (continua.lower() == 'q'):
                sys.exit()
            elif (continua.lower() == 'n'):
                os.system('clear')
                break
            else:
                print(f'Entrada inválida.')