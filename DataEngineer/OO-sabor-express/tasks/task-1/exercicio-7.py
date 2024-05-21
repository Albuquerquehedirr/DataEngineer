# 7-Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza place'
restaurante_pizza.categoria = 'Fast Food'

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_pizza))
#Resposta
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast food')
else:
    print('A categoria não é Fast Food')