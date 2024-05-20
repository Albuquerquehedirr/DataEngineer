#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

numeros = [1,2,3,4,5,6,7,8,9,10]
soma_dos_numeros_impares = 0


for numero in numeros:
    if numero % 2 != 0:
        soma_dos_numeros_impares += numero
        print('A soma dos números ímpares é: ',soma_dos_numeros_impares)