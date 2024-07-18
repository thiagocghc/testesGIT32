
lista_pessoas = [
	{'nome': 'Ana', 'idade': 30, 'cidade': 'São Paulo'},
	{'nome': 'João', 'idade': 25, 'cidade': 'Rio de Janeiro'},
	{'nome': 'Maria', 'idade': 35, 'cidade': 'Belo Horizonte'},
	{'nome': 'Pedro', 'idade': 28, 'cidade': 'Salvador'}
]

for item in lista_pessoas:
    print(item['nome']," - ", item['cidade'])