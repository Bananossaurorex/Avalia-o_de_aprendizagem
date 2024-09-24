import os
from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil
from projeto.models.enum.setor import Setor
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.unidadeFederativa import UnidadeFederativa
from projeto.models.fornecedor import Fornecedor
from projeto.models.medico import Medico
from projeto.models.engenheiro import Engenheiro
from projeto.models.advogado import Advogado
from projeto.models.cliente import Cliente

medico1 = Medico(42,"Luis",40028922,"@gmail.com",
                 Endereco("Rua maluca","18","1 andar","4040","Salvador",UnidadeFederativa.BAHIA),
                 Sexo.MASCULINO,EstadoCivil.VIUVO,"04/11/2005","cpf","rg","matricula",
                 Setor.SAUDE,10005.3,"crm")

engenheiro1 = Engenheiro(52,"Breno",95852255,"breno.@gmail.com",
                 Endereco("Rua louca","26","3 andar","1010","Salvador",UnidadeFederativa.BAHIA),
                 Sexo.MASCULINO,EstadoCivil.CASADO,"17/07/2004","cpf","rg","matricula",
                 Setor.ENGENHARIA,1454.4,"crea")

advogado1 = Advogado(19,"Rafael",385955,"rafael.@gmail.com",
                 Endereco("Rua doida","35","4 andar","2626","Salvador",UnidadeFederativa.BAHIA),
                 Sexo.MASCULINO,EstadoCivil.CASADO,"07/07/2001","cpf","rg","matricula",
                 Setor.JURIDICO,1556.2,"oab")

fornecedor1 = Fornecedor("Maria","40028922","maria.@gmail.com",
                 Endereco("Rua das pitanguinhas","15","5 andar","478134","Salvador",UnidadeFederativa.BAHIA),
                 "123450001","1718763","454589", "Luvas")

cliente1 = Cliente(89, "Roberto",156985,"roberto.@gmail.com",
                   Endereco("Rua A","98","9 andar","1597","Salvador",UnidadeFederativa.BAHIA),
                   Sexo.MASCULINO,EstadoCivil.CASADO,"04/10/1987", 4579)


os.system("clear")
print(medico1)
print(engenheiro1)
print(advogado1)
print(fornecedor1)
print(cliente1)