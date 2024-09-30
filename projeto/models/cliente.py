from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.fisica import Fisica

class Cliente(Fisica):
    def __init__(self ,id: int, nome: str, telefone: int, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil,dataNascimento: str,protocoloAtendimento: int) -> None:
        super().__init__(id,nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return f"{super().__str__()}\nProtocolo de Atendimento: {self.protocoloAtendimento}"