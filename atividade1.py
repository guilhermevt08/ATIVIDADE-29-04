import os 
from dataclasses import dataclass

os.system('cls')

@dataclass
class endereco:
    logradouro: str 
    numero: str

@dataclass
class cliente:
    nome: str
    idade: str
    endereco: endereco
    
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'endereco: {self.endereco.logradouro}')
        print(f'Número: {self.endereco.numero}')
    
    print('= Solicitado dados do cliente =')
cliente = cliente(
    nome =input('Digite seu nome: '),
    idade =int(input('Digite sua idade: ')),
    endereco = endereco(
        logradouro =input('Digite o endereco: '),
        numero =input('Digite o número: ')
    )
)

print('\n= Exibindo dados do cliente =')
cliente.mostrar_dados()