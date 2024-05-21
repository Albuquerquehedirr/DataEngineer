# 9-Imprima no console o nome e a categoria da instância restaurante_praca.
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
