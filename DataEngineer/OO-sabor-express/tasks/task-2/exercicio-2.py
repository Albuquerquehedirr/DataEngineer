# 2-Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    restaurantes = []
    def __init__(self,nome, categoria, ativo=False, acessibilidade=False, espaco_kids=False ):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.acessibilidade = acessibilidade
        self.espaco_kids = espaco_kids
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.acessibilidade} | {self.espaco_kids}'

restaurante01 = Restaurante('Karnivuros', 'Hamburgueria', True, False, True)
restaurante02 = Restaurante('Mantovanni', 'Hamburgueria', True, True, True)
print(restaurante01)
print(restaurante02)

