print('CADASTRO')
try:
    n = int(input('Informe o número de registros (1-16): '))
    print('Dados do funcionário')
    cont = 0
    L = []
    while cont < n:
        id = int(input('Id: '))
        nome = input('Nome: ')
        sexo = input('Sexo (M/F): ')
        cargo = input('Cargo: ')
        admissao = input('Data de admissão (dd/mm/aaaa): ')
        salario = float(input('Salário (0000.00): '))
        T = id, nome, sexo, cargo, admissao, salario
        L.append(T)
        cont += 1
        print()

    print('{:^10}'.format('Id'), end = '')
    print('{:^10}'.format('Nome'), end = '')
    print('{:^10}'.format('Sexo'), end = '')
    print('{:^10}'.format('Cargo'), end = '')
    print('{:^10}'.format('Admissão'), end = '')
    print('{:^10}'.format('Salário'))

    i = 0
    while i < n:
        j = 0
        while j < 6:
            print('{:^10}'.format(L[i][j]), end = '')
            j += 1
        print()
        i += 1
except:
    print('Valor numérico necessário!')