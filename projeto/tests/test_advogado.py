import pytest
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.setor import Setor
from projeto.models.enum.unidadeFederativa import UnidadeFederativa

@pytest.fixture
def criar_advogado():
    advogado = Advogado(1111, "Mara", 71988514981,"@gmail.com",
                Endereco("Rua das ruas","13","2 andar","42342","Salvador",UnidadeFederativa.BAHIA),
                Sexo.FEMININO,EstadoCivil.SOLTEIRO,"12/12/2012","0938891","2312344",
                "matricula",Setor.JURIDICO,1000.8,"oab")
    return advogado

def test_oab_invalido():
    with pytest.raises (TypeError,match = "OAB"):
        Advogado(12,"Luis",40028922,"@gmail.com",
    Endereco("Rua maluca","18","1 andar","4040","Salvador",UnidadeFederativa.BAHIA),
    Sexo.MASCULINO,EstadoCivil.VIUVO,"04/11/2005","cpf","rg","matricula",
    Setor.SAUDE,10005.3,"djbfijs")
