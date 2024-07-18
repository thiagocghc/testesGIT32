dici = {
    'id':'4',
    'nome':'Pera',
    'preco':11.90
}

lista = [
    {
    'id':'1',
    'nome':'Banana',

    'preco':4.7
},{
    'id':'2',
    'nome':'Mamao',
    'preco':6.5
},{
    'id':'3',
    'nome':'Uva',
    'preco':9.56
},{
    'id':'4',
    'nome':'Pera',
    'preco':11.90
}]

# for item in lista:
#     print(item['preco'])

# for key in dici.keys():
#     print(key)

# for val in dici.values():
#     print(val)

for key,val in enumerate(dici):
    print(key,val)