# 8-Mude o estado da instância restaurante_pizza para ativo.

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'
print(restaurante_praca.ativo)

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza place'
restaurante_pizza.categoria = 'Fast Food'

restaurante_pizza.ativo = True #resposta
restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_pizza.ativo)