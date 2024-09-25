from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.setor import Setor
from projeto.models.enum.sexo import Sexo
from projeto.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self,id: int, nome: str, telefone: int, email: str, endereco: Endereco,
                  sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str,
                    rg: str, matricula: str, setor: Setor, salario: float,crm: str) -> None:
        
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf,
                          rg, matricula, setor, salario)
        self.crm = self._verificarCRM(crm)

    def _verificarCRM(self,crm):
        if crm == "":
            raise ValueError("O nome não pode ser vazio")
        return crm

    def __str__(self) -> str:
        return f"{super().__str__()}\nCrm: {self.crm}"