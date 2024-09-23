from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa
from abc import ABC, abstractmethod

class Juridica(Pessoa,ABC):
    def __init__(self ,id: int, nome: str, telefone: int, email: str, endereco: Endereco,cnpj: str,inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual

    @abstractmethod
    def __str__(self) -> str:
        return f"{super().__str__()}\nCnpj: {self.cnpj}\nIncrição Estadual: {self.inscricaoEstadual}"