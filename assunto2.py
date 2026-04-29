import os
from dataclasses import dataclass

os.system('cls')
@dataclass
class funcionario:
    nome: str
    matricula: str
    salario: float
    email: str
    setor: str
    telefone: str 

funcionario1 = funcionario('Paulo', '777', 2500.00, 'pgvl@gmail.com', 'TI', '(71) 981088538')
print(f'nome: {funcionario1.nome}')
print(f'matricula: {funcionario1.matricula}')
print(f'salario: {funcionario1.salario}')
print(f'email: {funcionario1.email}')
print(f'setor: {funcionario1.setor}')
print(f'telefone: {funcionario1.telefone}')