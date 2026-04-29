import os
from dataclasses import dataclass

os.system('cls')
@dataclass
class cliente:
    nome: str
    email: str
    telefone: str

cliente1 = cliente('Paulo', 'pgvl@gmail.com', '71981088538')

print(f'nome: {cliente1.nome}')
print(f'email: {cliente1.email}')
print(f'telefone: {cliente1.telefone}')