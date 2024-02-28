class Cliente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.conta = None

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nCPF: {self.cpf}\nConta: {self.conta.numero if self.conta else 'N/A'}\nTipo de Conta: {self.conta.tipo if self.conta else 'N/A'}\nStatus: {'Aberta' if self.conta and self.conta.aberta else 'Fechada'}\nSaldo: {self.conta.saldo if self.conta else 0}"


class Conta:
    def __init__(self, tipo, numero):
        self.tipo = tipo
        self.numero = numero
        self.aberta = True
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def emprestimo_disponivel(self):
        return self.saldo * 2


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas_abertas = []

    def abrir_conta(self, nome, idade, cpf, tipo_conta):
        if any(cliente.cpf == cpf for cliente in self.clientes):
            print("Cliente já cadastrado")
            return

        if idade < 18:
            print("Cliente precisa ser maior de idade")
            return

        cliente = Cliente(nome, idade, cpf)
        conta = Conta(tipo_conta, len(self.contas_abertas) + 1)
        cliente.conta = conta
        self.clientes.append(cliente)
        self.contas_abertas.append(conta)

        print("Conta aberta com sucesso!")

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)
            print()

    def fazer_deposito(self, numero_conta, valor):
        conta = self.encontrar_conta(numero_conta)
        if conta:
            conta.depositar(valor)
            print("Depósito realizado com sucesso!")
        else:
            print("Conta não encontrada")

    def fazer_saque(self, numero_conta, valor):
        conta = self.encontrar_conta(numero_conta)
        if conta:
            if conta.sacar(valor):
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente")
        else:
            print("Conta não encontrada")

    def fechar_conta(self, numero_conta):
        conta = self.encontrar_conta(numero_conta)
        if conta:
            if conta.saldo == 0:
                conta.aberta = False
                print("Conta fechada com sucesso!")
            else:
                print("É necessário esvaziar a conta antes de fechá-la")
        else:
            print("Conta não encontrada")

    def fazer_emprestimo(self, numero_conta, valor):
        conta = self.encontrar_conta(numero_conta)
        if conta:
            if valor > conta.emprestimo_disponivel():
                print("Valor maior que o seu limite")
                return
            total_emprestado = sum(c.saldo for c in self.contas_abertas)
            if total_emprestado + valor > 0.2 * sum(c.saldo for c in self.contas_abertas):
                print("Valor maior que o crédito disponível nesta agência")
                return
            conta.depositar(valor)
            print("Empréstimo efetuado com sucesso!")
        else:
            print("Conta não encontrada")

    def encontrar_conta(self, numero_conta):
        for cliente in self.clientes:
            if cliente.conta and cliente.conta.numero == numero_conta:
                return cliente.conta
        return None


def main():
    banco = Banco()

    while True:
        print("\nMenu:")
        print("(1) Abrir conta")
        print("(2) Listar clientes")
        print("(3) Fazer depósito")
        print("(4) Fazer saque")
        print("(5) Fechar conta")
        print("(6) Fazer empréstimo")
        print("(7) Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome completo: ")
            idade = int(input("Digite a idade: "))
            cpf = input("Digite o CPF: ")
            tipo_conta = input("Digite o tipo de conta (conta corrente/conta poupança): ").lower()
            banco.abrir_conta(nome, idade, cpf, tipo_conta)

        elif opcao == "2":
            print("\nClientes:")
            banco.listar_clientes()

        elif opcao == "3":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a ser depositado: "))
            banco.fazer_deposito(numero_conta, valor)

        elif opcao == "4":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a ser sacado: "))
            banco.fazer_saque(numero_conta, valor)

        elif opcao == "5":
            numero_conta = int(input("Digite o número da conta: "))
            banco.fechar_conta(numero_conta)

        elif opcao == "6":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do empréstimo: "))
            banco.fazer_emprestimo(numero_conta, valor)

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()

# Separar as funções depois.
# Tentar simplificar mais ainda
# Última alteração em 02/01/2024