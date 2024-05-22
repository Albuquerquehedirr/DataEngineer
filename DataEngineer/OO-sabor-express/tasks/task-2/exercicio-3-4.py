# 3 e 4 -Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, acessibilidade, espaco_kids, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.acessibilidade = acessibilidade
        self.espaco_kids = espaco_kids
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.acessibilidade} | {self.espaco_kids} '

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(
                f'nome: {restaurante.nome} | categoria: {restaurante.categoria} | acessibilidade: {restaurante.acessibilidade}  | espaço_kids: {restaurante.espaco_kids} | ativo: {restaurante.ativo}')


restaurante01 = Restaurante('Karnivuros', 'Hamburgueria', True, False, True)
restaurante02 = Restaurante('Mantovanni', 'Hamburgueria', True, True, True)
Restaurante.listar_restaurantes()