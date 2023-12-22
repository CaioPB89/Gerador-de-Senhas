# importe as dependencias necessarias
from random import randint, choice
import string

#crie os grupos de caracteres que vamos usar
letrasMaio = string.ascii_uppercase
letrasMinus = string.ascii_lowercase
numeros = string.digits
simbolos = "!?/$&"

#concatene todos em só uma string
caracteresaceitaveis = letrasMaio + letrasMinus + numeros + simbolos
# gera um tamanho aleatorio
tamanho = randint(9, 12)


while True:
    # gera a senha vazia
    senha = ''
    # para cada espaço no tamanho
    for letter in range(tamanho):
        #concatene um caractere aleatorio na senha
        senha += ''.join(choice(caracteresaceitaveis))
    # checa se: tem um simbolo, um numero e uma maiuscula
    # no caso, vê se possui match entre os grupos de caracteres e a senha
    if any(char in simbolos for char in senha) and\
    any(char in numeros for char in senha)and\
    any(char in letrasMaio for char in senha):
        break

print(senha)

#salvando a senha criada em um arquivo
# txt = open("arquivodetestes.txt", "a")
# txt.write(f"\n{senha}")