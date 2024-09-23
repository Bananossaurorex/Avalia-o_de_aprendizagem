import os
from models.endereco import Endereco
from models.enum.estadoCivil import EstadoCivil
from models.enum.setor import Setor
from models.enum.sexo import Sexo
from models.enum.unidadeFederativa import UnidadeFederativa    
from models.fornecedor import Fornecedor
from models.medico import Medico

pessoa1 = Medico("Luis",40028922,"@gmail.com",
                 Endereco("Rua maluca","18","1 andar","4040","Salvador",UnidadeFederativa.BAHIA),
                 Sexo.MASCULINO,EstadoCivil.VIUVO,"04/11/2005","cpf","rg","matricula",
                 Setor.SAUDE,10005.3,"crm")
os.system("clear")
print(pessoa1)