import pytest
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.setor import Setor
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.unidadeFederativa import UnidadeFederativa
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco


@pytest.fixture
def criar_medico(): 
    medico = Medico(12,"Luis",40028922,"@gmail.com",
    Endereco("Rua maluca","18","1 andar","4040","Salvador",UnidadeFederativa.BAHIA),
    Sexo.MASCULINO,EstadoCivil.VIUVO,"04/11/2005","cpf","rg","matricula",
    Setor.SAUDE,10005.3,"crm")
    return medico


def test_nome_invalido_retorna_mensagem_excessao():
    with pytest.raises(ValueError, match = "O nome não pode ser vazio"):
       Medico(12,"","telefone","@gmail.com",
                Endereco("Rua maluca","18","1 andar","4040","Salvador",UnidadeFederativa.BAHIA),
                 Sexo.MASCULINO,EstadoCivil.VIUVO,"04/11/2005","cpf","rg","matricula",
                 Setor.SAUDE,10005.3,"crm")


def test_telefone_invalido():
   with pytest.raises(TypeError,match = "Coloque um telefone valido"):
    Medico(12,"Luis","telefone","@gmail.com",
                Endereco("Rua maluca","18","1 andar","4040","Salvador",UnidadeFederativa.BAHIA),
                 Sexo.MASCULINO,EstadoCivil.VIUVO,"04/11/2005","cpf","rg","matricula",
                 Setor.SAUDE,10005.3,"crm")

