class Conta:
    def __init__(self, cliente, agencia, numero, pix, saldo):
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        self.pix = pix
        self.saldo = saldo
        
    def deposita(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def extrato(self):
            print(f'Titular: {self.cliente.nome}\nCpf: {self.cliente.cpf}\nAgencia: {self.agencia}\nNumero: {self.numero}\nPix: {self.pix}\nSaldo: {self.saldo:.2f}\n')