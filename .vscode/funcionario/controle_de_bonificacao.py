class ControleDeBonificacao:
    def __init__(self):
        self._total_bonificacoes = 0

    def registra(self, funcionario):
        self._total_bonificacoes += funcionario.bonificacao

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes