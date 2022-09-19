nameBank = 'Banco HPS Sistemas'
print('=' * 10, {nameBank}, "=" * 10)

while True:
    id_nameUser = input("Nome: ")
    if all(c.isalpha() or c.isspace() for c in id_nameUser):  # faz com apenas aceita valores alfabéticos.
        break  # sai do while.
    else:
        print("Por favor digite um nome válido!")

# Usando key_customerUser para procurar clientes já cadastrado no sistema.
while True:
    key_custumerUser = " "
    while key_custumerUser not in 'SN':
        key_custumerUser = str(input("Possui cadastro: [S/N] ")).strip().upper()[0]
    if key_custumerUser == 'S' or 'N': # Se SIM ir para area de usuarios cadastrados (criar esta area)
        break

while True:
    id_registrationCPF = input("CPF: ")
    if all(c.isnumeric() for c in id_registrationCPF):  # faz com apenas aceita valores alfabéticos.
        break  # sai do while.
    else:
        print("Por favor digite um nome válido!")

while True:
    id_registrationRG = input("RG: ")
    if all(c.isnumeric() for c in id_registrationRG):  # faz com apenas aceita valores alfabéticos.
        break  # sai do while.
    else:
        print("Por favor digite um nome válido!")

print('''
\t[1] Masculino
\t[2] Feminino
\t[3] Transexual
\t[4] Prefiro não dizer
''')
key_selectSexo = input('Selecione uma das opções: ')
select1 = 1
select2 = 2
select3 = 3
select4 = 4
while True:
    try:
        if key_selectSexo == select1:
            print(f'{key_selectSexo} Masculino')
            break
        elif key_selectSexo == select2:
            print(f'{key_selectSexo} Feminino')
            break
        elif key_selectSexo == select3:
            print(f'{key_selectSexo} Transexual')
            break
        elif key_selectSexo == select4:
            print(f'{key_selectSexo} Prefiro não dizer')
            break
        else:
            key_selectSexo = int(input('Confirme novamente: '))
    except:
        print('Valor inválido!')

print('''Como você se identifica?
\t[1] Homem Cisgenero
\t[2] Mulher Cisgenera
\t[3] Homem Transgenero
\t[4] Mulher Transgenera
\t[5] Prefere não dizer
\t[6] Nenhuma das opções''')
input('Diga qual é o seu genêro? ')
print()

print('''Estado civil
\t [1] Solteiro(a)
\t [2] Casado(a)
\t [3] Viúvo(a)
\t [4] Divorciado(a)
\t [5] União Estável''')
select_status = str(input('Escolha uma das opções: '))
print()

id_numberPhone1 = int(input('Celular: '))
id_numberPhone2 = int(input('Tel. Residencial: '))
print()
id_adress = str(input('Endereço: '))
id_numberhouse = int(input('Número: '))
id_cep = int(input('CEP: '))
id_block = str(input('Bairro: '))
id_completeAdress = str(input('Complemento: '))
id_city = str(input('Cidade: '))
id_state = str(input('Estado: '))

# Pergunta de possui imóvel na cidade
while True:
    id_valueFunding1 = " "
    while id_valueFunding1 not in 'SN':
        id_valueFunding1 = str(input("Possui imóvel na cidade: [S/N] ")).strip().upper()[0]
    if id_valueFunding1 == 'S' or 'N':
        break


# Definindo minha função na area cadastro


