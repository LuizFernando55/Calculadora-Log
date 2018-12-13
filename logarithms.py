#coding: utf-8
__author__ = 'Luiz Fernando SS'
print("\033[34mMonte seu Logarítimo\033[m")
print("""Selecione o produto desejado: 
[ 1 ] Base
[ 2 ] Expoente
[ 3 ] Argumento""")
option = int(input("A opção desejada: "))
if option == 1:
    exp = float(input("Digite o expoente: "))
    arg = float(input("Digite o argumento: "))
    produto = arg**1/exp
if option == 2:
    base = float(input("Digite a base: "))
    arg = float(input("Digite o argumento: "))
    #Todo Descobrir o valor do expoente: de base e arg já definidos
if option == 3:
    base = float(input("Digite a base: "))
    exp = float(input("Digite o expoente: "))
    produto = base**exp
print("O Produto desse log foi:", produto)
