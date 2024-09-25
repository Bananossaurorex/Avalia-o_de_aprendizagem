import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.setor import Setor
from projeto.models.enum.unidadeFederativa import UnidadeFederativa


@pytest.fixture
def criar_medico():
    medico = Medico (12,"Luis",40028922,"@gmail.com",
    Endereco("Rua maluca","18","1 andar","4040","Salvador",UnidadeFederativa.BAHIA),
    Sexo.MASCULINO,EstadoCivil.VIUVO,"04/11/2005","cpf","rg","matricula",
    Setor.SAUDE,10005.3,12)
    return medico

def test_crm_invalido():
    with pytest.raises (ValueError,match = ""):
        Medico(12,"Luis",40028922,"@gmail.com",
    Endereco("Rua maluca","18","1 andar","4040","Salvador",UnidadeFederativa.BAHIA),
    Sexo.MASCULINO,EstadoCivil.VIUVO,"04/11/2005","cpf","rg","matricula",
    Setor.SAUDE,10005.3,"")

def test_confirmacao_id(criar_medico):
    assert criar_medico.id == 12
