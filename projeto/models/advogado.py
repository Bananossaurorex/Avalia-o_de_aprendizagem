from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.setor import Setor
from projeto.models.enum.sexo import Sexo
from projeto.models.funcionario import Funcionario

class Advogado(Funcionario):
    def __init__(self,id: int, nome: str, telefone: int, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, oab: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.oab = self._verificarOab(oab)

    def _verificarOab(self,oab):
        if not isinstance (oab,int):
            raise TypeError("OAB")
        return oab

    def __str__(self) -> str:
        return f"{super().__str__()}\nOab: {self.oab}"