# 1-Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False



# 2-Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f'A conta do {self.titular} possui saldo de R${self.saldo}'

# 3-Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

# conta1 = ContaBancaria('Hedir', 100)
# conta2 = ContaBancaria('Samuel', 500)
# conta3 = ContaBancaria('Maria', 3000)
# print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
# ContaBancaria.ativar_conta(conta3)
# print(f"Depois de ativar: Conta ativa? {conta3._ativo}")

# contas = [conta1, conta2]
# print(conta1)
# print(conta2)
# print(conta3)

# 4-Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

# @property
# def titular(self):
#     return self._titular
# @property
# def saldo(self):
#     return self._saldo
# @property
# def ativo(self):
#     return self._ativo

# 5 - Crie uma instância da classe e imprima o valor da propriedade titular.
# conta1 = ContaBancaria('Hedir', 100)
# print(conta1.titular)

# 6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, nome, agencia, profissao, cidade, saldo):
        self.nome = nome
        self.agencia = agencia
        self.profissao = profissao
        self.cidade = cidade
        self.saldo = saldo

    def __str__(self):
        # return f'{self.nome} | {self.agencia} | {self.cidade} | {self.profissao} | {self.saldo}'
        return f'O nome do titular da conta é {self.nome} lotada na agência de n° {self.agencia}, residente na cidade de {self.cidade}, de profissão {self.profissao}, com o saldo atual de {self.saldo}'


# cliente1 = ClienteBanco('Maria', 100, 'Desenvolvedor', 'Itu', '1000')
# cliente2 = ClienteBanco('João', 500, 'Químico', 'Santos', '2000')
# cliente3 = ClienteBanco('Paulo', 10, 'Escritor', 'Sorocabal', '3000')

# print(f"Cliente 1: Nome: {cliente1.nome}, Idade: {cliente1.agencia}, Profissão: {cliente1.profissao}, Cidade: {cliente1.cidade}, Saldo: {cliente1.saldo}")

# 7 -Crie um método de classe para a conta ClienteBanco

    @classmethod
    def criar_conta(cls, nome,agencia, profissao, cidade,saldo):
        return cls(nome, agencia, profissao, cidade, saldo)

# cliente1 = ClienteBanco('Maria', 100, 'Desenvolvedor', 'Itu', '1000')
# cliente2 = ClienteBanco('João', 500, 'Químico', 'Santos', '2000')
# cliente3 = ClienteBanco('Paulo', 10, 'Escritor', 'Sorocabal', '3000')

#print(f"Cliente 1: Nome: {cliente1.nome}, Idade: {cliente1.agencia}, Profissão: {cliente1.profissao}, Cidade: {cliente1.cidade}, Saldo: {cliente1.saldo}")

# preciso chamar o classmethod

criar_cliente1 = ClienteBanco.criar_conta('Maria', 100, 'Desenvolvedor', 'Itu', '1000')
print(criar_cliente1)