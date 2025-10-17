from ifrn.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self._siape = siape