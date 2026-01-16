# Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

dicio = {'Nome': "Guilherme", 'Idade': 18, 'Cidade': "São Paulo"}
print(f"\nDicionário desatualizado: {dicio}")

# Atualizando a idade
dicio.update({'Idade': 19})

# Adicionando a profissão
dicio['Profissão'] = "Auxiliar Administrativo"

# Removendo um item do dicionário
del dicio['Cidade']

print(f"\nDicionário atualizado: {dicio}")