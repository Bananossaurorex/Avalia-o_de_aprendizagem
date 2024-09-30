import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.unidadeFederativa import UnidadeFederativa

@pytest.fixture
def criar_fornecedor():
    fornecedor = Fornecedor(111,"Geraldo",222,"geraldonho",Endereco("Rua Trans","3 milhões","2° andar","346457","Copacabana",UnidadeFederativa.RIO_DE_JANEIRO),
                            "cnpj","43234","Sapatos")
    return fornecedor
    
def test_confirmacao_produto(criar_fornecedor):
    assert criar_fornecedor.produto == "Sapatos"