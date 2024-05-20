#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

number = int(input('Informe um número: \n'))
if number % 2 == 0:
        print(f'O número {number} é par.')
else:
        print(f'O numéro {number} é ímpar.')