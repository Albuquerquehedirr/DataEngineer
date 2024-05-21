# 2-Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça' # "resposta do exercício" atribuindo o valor solicitado ao atributo categoria da instância restaurante_praca da classe restaurante.

restaurantes = [restaurante_praca]
print(vars(restaurante_praca))
