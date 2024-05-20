# #2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

age = int(input('Informe a idade: \n'))
if age >= 0 and age <= 12:
        print('É uma criança')
elif age >= 13 and age <= 18:
        print('É um adolescente')
elif age > 18:
        print('É um adulto')
else:
        print('Idade inválida')