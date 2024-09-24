from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self,id: int,nome: str, telefone: int, email: str, endereco: Endereco) -> None:
        self.id = id
        self.nome = self._verificarNome(nome)
        self.telefone = self._verificarTelefone(telefone)
        self.email = email
        self.endereco = endereco
    
    
    
    def _verificarNome(self,nome):
        if nome == "":
            raise ValueError("O nome não pode ser vazio")
        return nome
    
    def _verificarTelefone(self,telefone):
        if not isinstance (telefone,int):
            raise TypeError("Coloque um telefone valido")
        return telefone

    @abstractmethod
    def __str__(self) -> str:
        return (f"ID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\n--Endereco--\n{self.endereco}"
        )