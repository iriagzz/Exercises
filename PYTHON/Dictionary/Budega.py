class Clientes():
    def __init__(self, nome,  divida):
        self.nome = nome
        self.divida = divida


class Budega():
    def __init__(self):
        self.clientes = {}

    def cadastrar_clientes(self,):
        print('****** Cadastrar Cliente ******')
        nome = input('Nome: ').upper()
        if nome in self.clientes.keys():
            print("Cliente já cadastrado")
        else:
            divida = int(input('Saldo Devido: '))
            cliente = Clientes(nome, divida)
            self.clientes[cliente.nome] = cliente.divida

    def consulta_cliente(self):
        print('****** Consultar Cliente ******')
        nome = input('Nome: ').upper()
        if nome in self.clientes.keys():
            print('Cliente:', nome, 'Saldo: R$', self.clientes[nome])
        else:
            print('Cliente não cadastrado!')

    def cadastrar_divida(self):
        print('****** Cadastrar Dívida ******')
        nome = input('Nome: ').upper()
        if nome in self.clientes.keys():
            divida = int(input('Valor para acrescentar: '))
            self.clientes[nome] += divida
            print('Cliente:', nome, 'Saldo Atual: R$', self.clientes[nome])
        else:
            print('Cliente não cadastrado!')

    def cadastrar_pagamento(self):
        print('****** Cadastrar Pagamento ******')
        nome = input('Nome: ').upper()
        if nome in self.clientes.keys():
            divida = int(input('Valor para reduzir: '))
            self.clientes[nome] -= divida
            print('Cliente:', nome, 'Saldo Atual: R$', self.clientes[nome])
        else:
            print('Cliente não cadastrado!')

    def listar_caloteiros(self):
        print('****** Lista de Caloteiros ******')
        for item in self.clientes.items():
            print(item)

    def remover_cliente(self):
        print('****** Remover Caloteiro ******')
        nome = input('Nome: ').upper()
        self.clientes.pop(nome)

def menu():
    print('[1] - CADASTRAR CLIENTE\n[2] - CONSULTAR CLIENTE\n[3] - CADASTRAR DÍVIDA'
          '\n[4] - CADASTRAR PAGAMENTO\n[5] - LISTAR CALOTEIROS\n[6] - REMOVER CALOTEIRO\n[7] - SAIR')

def main():
    budega = Budega()

    run = True
    while run:
        menu()
        opcao = int(input('O que desejas fazer? '))
        if opcao == 1:
            budega.cadastrar_clientes()
        if opcao == 2:
            budega.consulta_cliente()
        if opcao == 3:
            budega.cadastrar_divida()
        if opcao == 4:
            budega.cadastrar_pagamento()
        if opcao == 5:
            budega.listar_caloteiros()
        if opcao == 6:
            budega.remover_cliente()
        if opcao == 7:
            run = False
main()