# Variables and constants

'''

'''
#concatenate
age = 28
name = "Bruno"

print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

age, name = (28, 'Bruno')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

# constant
'''
não existe constante em python, mas existe convenção

ex: ABS_PATH = 'dasdasddssdadd/dsadas/dsad'
DEBUG = False
STATES = [
    'SP',
    'RJ',
    'MG',
]

AMOUNT = 2.25
'''

# Boas práticas em python
# usar snakecase   teste_do_teste
# nomes de constantes sempre maiusculo 

# converção de tipos
# float para inteiro

preco = 10.30
print(preco)

preco = int(preco)
print(preco)

# conversão por divisão

preco = 10
print(preco)

print(preco / 2)
# saida 5.0

print(preco // 2)
#saida 5