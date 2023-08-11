'''
Exemplos de aula pratica de Dicionarios
'''
pessoas = {'nome': 'Janio', 'sexo': 'M', 'idade': 21}
print(pessoas)
print(pessoas['nome']) #keys elemetos
print()
'-------------------------------------------------'
# na hora de referênciar elementos com dicionarios devemos usar aspas duplas ""
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') 
print()
'----------------------------------------------------'
'Usando metódos internos'
print(pessoas.keys())
print()
print(pessoas.values())
print()
'Mostra um composição interna  3 tupla nome sexo e idade lista dicionário'
print(pessoas.items())
print()
'---------------------------'

for k in pessoas.keys():
    print(k)# exibe os elementos, keys
print()
for c in pessoas.values():
    print(c) # exibe os valores 
print()
for t in pessoas.items() :
    print(f'{t}')
print()
# Dicionarios não se usa "enumerate"
for k ,v in pessoas.items() :
    print(f'{k} = {v}')
print()
'----------------------------'
# Trocando o valores associados  (values), aos indetificadores (keys/elementos)
pessoas['nome'] = 'Dayane'
for k ,v in pessoas.items() :
    print(f'{k} = {v}')
print()
'-----------------'
# Como adicionar keys/elementos , e valores(values).
pessoas['peso'] = 68.9
for k ,v in pessoas.items() :
    print(f'{k} = {v}')
print()
#----------------------------
# apaguar keys/elementos
del pessoas['sexo']
for k ,v in pessoas.items() :
    print(f'{k} = {v}')
print()
'-----------------'
#Criando lista com dicionários
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'Rj'}
estado2 = {'uf': 'São Paulo', 'sigla': 'Sp'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil) # exibe a lista com dois elementos
print
print(brasil[0]["sigla"])
print(brasil[1]["sigla"])
print()
'-----------------'
brasil.clear() # Abordagem para remover todos o itens
print(brasil)
print
'-----------'
# 

brasil = []
# não foi possivél usar dict para declarar e muito menos chaves antes do for
for c in range(3):
    estado = {}
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] =str(input('Sigla: '))
    brasil.append(estado.copy())
for lista in brasil:
    print(lista) # Exibi a três listas em diconario separado
print('-=-'*10)
# Uso de lalo for duplo para iterar sobre os itens do dicionários.
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} têm valor {v} !.')
print('-=-'*10)
'----------------------'
# Declarar tudo o contéudo dos diconarios, já dentro de uma lista !
brasil = [
    {'uf': 'São Paulo', 'sigla': 'SP'},
    {'uf': 'Rio de Janeiro', 'sigla': 'RJ'},
    {'uf': 'Minas Gerais', 'sigla': 'MG'}
]

for e in brasil:
    for v in e.items():
        print(f'O Campo {v} .')