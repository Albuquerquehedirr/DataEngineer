# 5-Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente:
    clientes = []
    def __init__(self, nome, idade, sexo, cidade):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cidade = cidade
        Cliente.clientes.append(self)
    def __str__(self):
        return f'{self.nome} {self.idade} {self.sexo} {self.cidade}'
    def exibir_informacoes_cliente():
        for cliente in Cliente.clientes:
            print(f'Nome: {cliente.nome}, Idade: {cliente.idade}, Sexo: {cliente.sexo}, Cidade: {cliente.cidade}')

cliente = Cliente('Hedir', '35', 'Masculino', 'Itu')
Cliente.exibir_informacoes_cliente()




