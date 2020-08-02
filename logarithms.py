# coding: utf-8
__author__ = 'Luiz Fernando SS'
# Logarithms_v2

from math import log

print("\033[34mMonte seu Logarítimo\033[m")

print("""Selecione a incógnita desejada: 
[ 1 ] Base
[ 2 ] Logaritmo
[ 3 ] Logaritmando""")

option = int(input("\nA opção desejada: "))

def verify_conditions(base, arg):
    if base <= 0 or base == 1 or arg <= 0:
        raise Exception("As Condições de Existência foram violadas")

if option == 1:
    exp = float(input("Digite o logarítmo: "))
    arg = float(input("Digite o logaritmando: "))

    result = arg**(1/exp)

if option == 2:
    base = float(input("Digite a base: "))
    arg = float(input("Digite o logaritmando: "))

    verify_conditions(base, arg)
    exp = log(arg) / log(base)

    result = exp

if option == 3:
    base = float(input("Digite a base: "))
    exp = float(input("Digite o logaritmo: "))

    result = base**exp

unknowns = ["A Base", "O Logaritmo", "O Logaritmando"]
str = unknowns[option - 1]

print("\n"+str+" desse log foi:", result)

