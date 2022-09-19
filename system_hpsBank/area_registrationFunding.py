from pyUFbr.baseuf import ufbr

# Campo para digitar dados para simulação do Financiamento
nameBank = 'Banco HPS Sistemas'
print('=' * 10, {nameBank}, '=' * 10)
print(f'Simulação de Financiamento Habitacional')

id_typeFunding = input("Tipo de financiamento: ")

print('''\t
   \t [1]  Financiamento
   \t [2]  Consórcio

''')

key_itemFunding = 1
key_itemConsortium = 2

while True:
    id_user = input('Digite o tipo de financiamento: ')
    if id_user == '1':
        print()

id_valueFunding = float(input('Valor aproximado do imóvel: '))
id_state = input('Estado:')
id_city = input('Município/Cidade: ')
id_salary = float(input('Informe a renda: '))

# Peido de Autorização de armazenamento de dados
while True:
    key_autorize = " "
    while key_autorize not in 'SN':
        key_autorize = str(input("Autorizo o Banco HPS Sistemas a coletar e armazenar meus dados pessoais, a enviar notificações e concordo com a Política de Privacidade. [S/N] ")).strip().upper()[0]
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
            "Você tem ou gostaria de ter crédito salário no Banco HPS ou produto de previdência? [S/N] ")).strip().upper()[
            0]
    if key_creditSalary == 'S':
        break

# Pergunta se é Servidor Público
while True:
    key_publicSever = " "
    while key_publicSever not in 'SN':
        key_publicSever = str(input("Algum dos participantes é Servidor Público? [S/N] ")).strip().upper()[0]
    if key_publicSever == 'S' or 'N':
        break
