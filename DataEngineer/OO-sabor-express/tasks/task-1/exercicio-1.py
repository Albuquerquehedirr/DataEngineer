# 1-Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
class Restaurante: # criação da classe e dos atributos
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana' # "resposta do exercício" atribuindo o valor solicitado ao atributo categoria da instância restaurante_praca da classe restaurante.

restaurantes = [restaurante_praca]
print(vars(restaurante_praca))
