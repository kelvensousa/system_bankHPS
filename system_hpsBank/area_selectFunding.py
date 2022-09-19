nameBank = 'Banco HPS Sistemas'
print('=' * 10, {nameBank}, '=' * 10)
print('''\t
   \t [1]  Habitacional
   \t [2]  Veículos
   \t [3]  Serviços
   \t [4]  Eletrodomésticos
   \t [5]  Eletrónicos
   \t [6]  Viagens
''')

item_housing = 1
item_cars = 2
item_services = 3
item_eletroNic = 4
item_eletroDom = 5
item_trips = 6

while True:
    id_user = input('Digite o tipo de financiamento: ')
    if id_user == '1':
        print()
        while True:
            print('''Escolha o tipo de imóvel
\t [1] [Novo]
\t [2] [Usado]
''')
            item_newHouse = 1
            item_oldHouse = 2
            id_user = input('Qual melhor se encaixa com você? ')
            if id_user == '1':
                print('''\t
\t  [1]  'Financiamento Casa Verde e Amarela/Pró Cotista - Recursos FGTS'
\t  [2]  'CIPH(Crédito Imobiliário Poupança HPS): Relacionamento + Crédito Salário com o HPS'
\t  [3]  'TPxF(TR, IPCA ou Tx FIXA): Relacionamento + Crédito Salário com o HPS'
\t  [4]  'CIPH(Crédito Imobiliário Poupança HPS): Vinc. Empreend. Financ no HPS - Relacionamento'
\t  [5]  'TPxF(TR, IPCA ou Tx FIXA): Vinc. Empreend. Financ no HPS - Relacionamento
''')
            break
