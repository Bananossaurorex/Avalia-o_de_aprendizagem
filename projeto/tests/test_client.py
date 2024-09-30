import pytest
from projeto.models.cliente import Cliente
from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.unidadeFederativa import UnidadeFederativa

@pytest.fixture
def criar_cliente():
    cliente = Cliente(666,"Robero",12,"roberto@gmail.com",Endereco("Rua fanática","123","1° andar","40","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,EstadoCivil.CASADO,"12/2/2004",12)
    return cliente
    
def test_confirmacao_nome(criar_cliente):
    assert criar_cliente.id == 666