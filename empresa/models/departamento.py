from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Optional 

@dataclass
class Departamento:

    _numero: Optional[int] = None
    _nome: str
    _cpf_gerente: Optional[str] = None
    _data_ini: date
    _created_at: Optional[datetime] = None
    _updated_at: Optional[datetime] = None

    # Funcionario -> JSON (dict)
    def to_dict(self) -> dict:
        return asdict(self)

    # JSON (dict) -> Funcionario
    @classmethod
    def from_dict(self, data: dict) -> 'Departamento':
        return Departamento(
            data.get('numero'),
            data.get('nome'),
            data.get('cpf_gerente'),
            data.get('data_ini'),
            data.get('created_at'),
            data.get('updated_at'),
        )
    
    def __str__(self) -> str:
        return (
            f'Funcionario(cpf={self._numero}, pnome={self._nome}, unome={self._cpf_gerente}, '
            f'data_nasc={self._data_ini}, endereco={self._created_at}, salario={self._updated_at})'
        )

    @property
    def numero(self) -> Optional[str]:
        return self._numero

    @numero.setter
    def numero(self, numero: Optional[str]):
        self._numero = numero
        self._updated_at = datetime.now()

    @property
    def nome(self) -> Optional[int]:
        return self._nome

    @nome.setter
    def nome(self, nome: Optional[int]):
        self._nome = nome
        self._updated_at = datetime.now()

    @property
    def cpf_gerente(self) -> Optional[int]:
        return self._cpf_gerente

    @cpf_gerente.setter
    def cpf_gerente(self, cpf_gerente: Optional[int]):
        self._cpf_gerente = cpf_gerente
        self._updated_at = datetime.now()

    @property
    def data_ini(self) -> Optional[int]:
        return self._data_ini

    @data_ini.setter
    def data_ini(self, data_ini: Optional[int]):
        self._data_ini = data_ini
        self._updated_at = datetime.now()

    @property
    def created_at(self) -> Optional[datetime]:
        return self._created_at

    @property
    def updated_at(self) -> Optional[datetime]:
        return self._updated_at