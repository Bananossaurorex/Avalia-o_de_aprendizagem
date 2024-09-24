import pytest
from ..models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.setor import Setor
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.unidadeFederativa import UnidadeFederativa
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco

@pytest.fixture
def criar_engenheiro(): 
    engenheiro = Engenheiro(12,"Luis",40028922,"@gmail.com",
    Endereco("Rua maluca","18","1 andar","4040","Salvador",UnidadeFederativa.BAHIA),
    Sexo.MASCULINO,EstadoCivil.VIUVO,"04/11/2005","cpf","rg","matricula",
    Setor.SAUDE,10005.3,12)
    return engenheiro

def test_crea_invalido():
    with pytest.raises (TypeError,match = "CREA"):
        Engenheiro(12,"Luis",40028922,"@gmail.com",
    Endereco("Rua maluca","18","1 andar","4040","Salvador",UnidadeFederativa.BAHIA),
    Sexo.MASCULINO,EstadoCivil.VIUVO,"04/11/2005","cpf","rg","matricula",
    Setor.SAUDE,10005.3,"djbfijs")
