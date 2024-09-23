from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.estadoCivil import EstadoCivil
from abc import ABC, abstractmethod

class Fisica(Pessoa,ABC):
    def __init__(self ,id: int, nome: str, telefone: int, email: str, endereco: Endereco,sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str) -> None:
        super().__init__(id,nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento

    @abstractmethod
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nSexo: {self.sexo}"
            f"\nEstado Civil: {self.estadoCivil}"
            f"\nData de Nascimento: {self.dataNascimento}"            
            )