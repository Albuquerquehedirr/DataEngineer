#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

login_esperado = 'Admin'
password_esperada = 'Password'

login = input("Informe o seu Login: ")
password = input("Informe a senha: ")

if login == login_esperado and password == password_esperada:
        print('Acesso Permitido')
else:
        print('Acesso Negado\nNome de usuário ou senha incorretos')