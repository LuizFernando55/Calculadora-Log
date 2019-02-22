# coding: utf-8
__author__ = 'Luiz Fernando SS'
# Logarithms_v2

print("\033[34mMonte seu Logarítimo\033[m")

print("""Selecione o produto desejado: 
[ 1 ] Base
[ 2 ] Expoente
[ 3 ] Argumento""")

option = int(input("A opção desejada: "))

if option == 1:
    exp = int(input("Digite o expoente: "))
    arg = int(input("Digite o argumento: "))

    produto = arg**1/exp

if option == 2:
    base = int(input("Digite a base: "))
    arg = int(input("Digite o argumento: "))

    exp = 0
    for e in range(0, arg, base):
        exp += 1

    produto = exp

if option == 3:
    base = int(input("Digite a base: "))
    exp = int(input("Digite o expoente: "))

    produto = base**exp

print("O Produto desse log foi:", produto)

