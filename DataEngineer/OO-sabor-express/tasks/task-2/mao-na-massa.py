# 0-Agora é sua vez! Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python.
# class Musica:
#     nome = ''
#     artista = ''
#     duracao = int


class Musica:

    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome}, Artista: {self.artista}, Duração: {self.duracao} segundos'

musica1 = Musica(nome='FreeBird', artista='Lynyrd Skynyrd', duracao=540)
print(musica1)


