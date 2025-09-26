## Programação com Acesso a Banco de Dados
# Revisão de Orientação a Objetos
# Prof. Guilherme Leal Santos


###Aula 12/09/2025 - Listas e Funções lambda
'''##Criar e visualizar listas
frutas = ['Maçã', 'Banana', 'Laranja']
print(frutas)
print(frutas[0])
print(f'Tamanho: {len(frutas)}')

##Adicionar elementos em uma lista
frutas.append('Uva')
print(frutas)
frutas.insert(1, 'Abacaxi')
print(frutas)

##Remover elementos em uma lista
# -> Remove ultimo elemento da lista
# fruta frutas.pop()
# -> Remove elemento do indice 0
# fruta = frutas.pop(0)
# -> Remove elemento pelo nome
# frutas.remove('Uva')
fruta = frutas.pop(0)
print(f'Removido: {fruta}')
print(frutas)

##Lista de numeros
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numeros)

# Ordenar - crescente
numeros_ord_c = sorted(numeros)
print(f'Lista ordenada (c): {numeros_ord_c}')
# Ordenar - decrescente
numeros_ord_d = sorted(numeros, reverse=True)
print(f'Lista ordenada (d): {numeros_ord_d}')

##Dobrando os numeros
# numeros_dobrados = []
# for n in numeros:
#    numeros_dobrados.append(n*2)
numeros_dobrados = list(map(lambda n: n*2, numeros))
print(numeros_dobrados)

##Numeros filtrados
# numeros_filtrados = []
# for n in numeros:
#     if n > 4:
#         numeros_filtrados.append(n)
numeros_filtrados = list(filter(lambda n: n > 4, numeros))
print(numeros_filtrados)

##Soma de todos os elementos da lista
# soma = 0
# for n in numeros:
#     soma += n
from functools import reduce
#Soma começando com 1
# soma = reduce(lambda soma, n: soma + n, numeros, 1)
#Soma começando com 0
soma = reduce(lambda soma, n: soma + n, numeros,)
print(soma)'''


###Aula 19/09/2025 - Orientação a Objetos
from conta import Conta
from cliente import Cliente
'''
cliente1 = Cliente('Elvis Presley', '111.222.333-44')
conta1 = Conta(cliente1, 1, 123, 'elvis@gmail.com', 12345678)
conta1.extrato()
# conta1.deposita(100)
# conta1.extrato()

# conta2 = conta1
# conta2.extrato()
# conta2.saca(100)
# conta2.extrato()
# conta1.extrato()

# if(conta1.saca(1000)):
#     print('OK')
# else:
#     print('Tá Liso')

cliente2 = Cliente('Jonhny Cage', '222.333.444-55')
conta2 = Conta(cliente2, 2, 234, 'jonhnny@outlook.com', 234567)
conta2.extrato()

if(conta2.transfere(conta1, 1000)):
    print('OK')
else:
    print('Tá liso')
'''
# Aula 26/09 - agregação, compisição e modificadores de acesso
cliente1 = Cliente('Elvis Presley', '111.222.333-44')
conta1 = Conta(cliente1, 1, 123, 'elvis@gmail.com', 12345678)
conta1.extrato()
conta1.saca(500)
conta1.deposita(300)

cliente2 = Cliente('Jonhny Cage', '222.333.444-55')
conta2 = Conta(cliente2, 2, 234, 'jonhnny@outlook.com', 234567)
conta2.extrato()
conta2.saca(100)
conta2.deposita(600)

conta1.transfere(conta2, 2000)
conta2.saca(10000)

conta1.historico.imprime()
conta2.historico.imprime()

# sem decorator
print(conta1.get_saldo())

# com decorator
print(conta1.saldo)

print(conta1.saldo+conta2.saldo)