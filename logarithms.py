# coding: utf-8
__author__ = 'Luiz Fernando SS'
# Logarithms_v2

from math import log

print("\033[34mMonte seu Logarítimo\033[m")

option = 0


def options():
    if option == 0:
        print("""Selecione a incógnita desejada: 
        [ 1 ] Base
        [ 2 ] Logaritmo
        [ 3 ] Logaritmando
        [ 4 ] Condições""")

        op = int(input("\nA opção desejada: "))

        return op


def conditions():
    if option == 4:
        print("""Condições para Criação do Logarítimo:

        base > 0
        base != 1
        logaritmando > 0""")

        input("\nPressione enter para continuar...\n")

        return 0
    else:
        logarithms()


def verify_conditions(base, arg):
    if base <= 0 or base == 1 or arg <= 0:
        raise Exception("As Condições de Existência foram violadas")


def logarithms():
    if option == 1:
        exp = float(input("Digite o logarítmo: "))
        arg = float(input("Digite o logaritmando: "))

        result = arg ** (1 / exp)
        verify_conditions(result, arg)

    if option == 2:
        base = float(input("Digite a base: "))
        arg = float(input("Digite o logaritmando: "))

        verify_conditions(base, arg)
        exp = log(arg) / log(base)

        result = exp

    if option == 3:
        base = float(input("Digite a base: "))
        exp = float(input("Digite o logaritmo: "))

        result = base ** exp
        verify_conditions(base, result)

    unknowns = ["A Base", "O Logaritmo", "O Logaritmando"]
    name = unknowns[option - 1]

    print("\n" + name + " desse log foi:", result)


while option == 0:
    option = options()
    option = conditions()


