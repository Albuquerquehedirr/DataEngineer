# 6-Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

#resposta
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza place'
restaurante_pizza.categoria = 'Fast Food'

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_pizza))