# 5-Altere o valor do atributo nome para 'Bistrô'.
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'
#resposta
restaurante_praca.nome = 'Bistrô'
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))