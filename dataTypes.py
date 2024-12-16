# comentário de linha

'''
comentário de linhas multiplas
'''

'''
Tipos básicos em Python

string = str 
numérico = int, float  10.50   100.000, complex
sequência = list, tuple, range
Mapa = dict,
Coleção = set, fronzenset
Boolean = bool True or False, 0 or 1
Binário = bytes, bytearray,memoryview
'''

#exemplos
# str
string = "Olá, Mundo!"
print(string)

# int
num_inteiro = 10
print(num_inteiro)

# float
num_flutuante = 10.50
print(num_flutuante)

# complex
num_complexo = 3 + 4j
print(num_complexo)

#list 
lista = [1, 2, 3, 4, 5]
print(lista)

#tuple
tupla = (1, 2, 3, 4, 5)
print(tupla)

#Range
sequencia = range(5)
print(list(sequencia))  # converte para lista para visualização

#Mapa (dict)
dicionario = {"nome": "João", "idade": 30}
print(dicionario)

#Coleção (set)
conjunto = {1, 2, 3, 4, 5}
print(conjunto)

#frozenset
frozenset_exemplo = frozenset([1, 2, 3, 4, 5])
print(frozenset_exemplo)


#bool
booleano = True
print(booleano)

#bool com numérico
booleano_2 = 1  # 1 é considerado True
print(bool(booleano_2))

#Binário
#bytes
bytes_exemplo = b"Texto em bytes"
print(bytes_exemplo)

#bytearray
bytearray_exemplo = bytearray([65, 66, 67])
print(bytearray_exemplo)

#memoryview
memoryview_exemplo = memoryview(bytes_exemplo)
print(memoryview_exemplo)

