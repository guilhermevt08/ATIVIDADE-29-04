import os
from dataclasses import dataclass

os.system('cls')
@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
print('= Solicitado dados do cliente =')
cliente =   Cliente(
nome =input('Digite seu nome: '),
email =input('Digite seu email: '),
telefone =input('Digite seu telefone: ')
)
print('- Exibindo dados do cliente -')
print(f'Nome: {cliente.nome}')
print(f'Email: {cliente.email}')
print(f'Telefone: {cliente.telefone}')