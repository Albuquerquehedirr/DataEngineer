# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
pessoa = {'nome': 'Hedir', 'idade': 28, 'cidade': 'Guarujá'}

pessoa['cidade'] = 'Itu'
print('Alteração da cidade: ',pessoa)
pessoa['profissão'] = 'Engenheiro de dados'
print('Adição do campo de profissão: ',pessoa)
del pessoa['cidade']
print('Exclusão do item cidade: ',pessoa)