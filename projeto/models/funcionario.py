import os
from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.fisica import Fisica
from projeto.models.enum.setor import Setor

class Funcionario(Fisica,ABC):
    def __init__(self,id: int,  nome: str, telefone: int, email: str, endereco: Endereco,
                  sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str,
                    cpf: str, rg: str,matricula: str,setor: Setor, salario: float) -> None:
        
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario


    @abstractmethod
    def __str__(self) -> str:
        return (
                f"{super().__str__()}"
                f"Cpf: {self.cpf}"
                f"\nRg: {self.rg}"
                f"\nMatricula: {self.matricula}"
                f"\nSetor: {self.setor.name}"
                f"\nSalario: {self.salario}"
                )