# 4-Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
class Restaurante:
    nome = ''
    categoria = 'Doces'
    ativo = False

categoria = Restaurante.categoria  # resposta
print(categoria)

