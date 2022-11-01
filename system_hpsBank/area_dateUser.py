# Inserir dados do CPF
while True:
    id_user = input('Qual é o seu CPF? ')
    if id_user.isnumeric():
        break
    continue

# Inserir dados de telefone
while True:
    id_user = input('Qual é o número do seu telefone celular? ')
    if id_user.isnumeric():
        break
    continue

# Inserir dados de renda
while True:
    id_user = input('Qual valor da renda bruta familiar mensal? ')
    if id_user.isnumeric():
        break
    continue

# Inserir data de nascimento
while True:
    id_user = input('Data de nascimento ')
    if id_user.isnumeric():
        break
    continue

# Pedido de Autorização de armazenamento de dados
while True:
    key_autorize = " "
    while key_autorize not in 'SN':
        key_autorize = str(input("Autorizo o Banco Nióbioo a coletar e armazenar meus dados pessoais, a enviar notificações e concordo com a Política de Privacidade. [S/N] ")).strip().upper()[0]
    if key_autorize == 'S':
        break

# Adicionando mais um dependente
while True:
    key_plusPeople = " "
    while key_plusPeople not in 'SN':
        key_plusPeople = str(input("Possui mais de um comprador e/ou dependente na proposta? [S/N] ")).strip().upper()[
            0]
    if key_plusPeople == 'S' or 'N':
        break

# Adicionando tempo de FGTS
while True:
    key_fgts = " "
    while key_fgts not in 'SN':
        key_fgts = str(input(
            "Possui mais de 3 anos de trabalho sob regime do FGTS, somando todos os períodos trabalhados? [S/N] ")).strip().upper()[
            0]
    if key_fgts == 'S' or 'N':
        break

# Autorizando o relacionamento com o banco
while True:
    key_autorizeRelation = " "
    while key_autorizeRelation not in 'SN':
        key_autorizeRelation = \
            str(input("Você gostaria de ter um relacionamento com o Banco HPS? [S/N] ")).strip().upper()[0]
    if key_autorizeRelation == 'S' or 'N':
        break

# Crédito Salário
while True:
    key_creditSalary = " "
    while key_creditSalary not in 'SN':
        key_creditSalary = str(input(
            "Você tem ou gostaria de ter crédito salário no Banco Nióbioo ou produto de previdência? [S/N] ")).strip().upper()[
            0]
    if key_creditSalary == 'S':
        break

# Perguntar se é Servidor Público
while True:
    key_publicSever = " "
    while key_publicSever not in 'SN':
        key_publicSever = str(input("Algum dos participantes é Servidor Público? [S/N] ")).strip().upper()[0]
    if key_publicSever == 'S' or 'N':
        break

