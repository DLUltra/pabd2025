from ifrn.pessoa import Pessoa

class ExAluno(Pessoa):
    def __init__(self, nome, cpf, siape):
        super().__init__(nome, cpf)
        self._siape = siape