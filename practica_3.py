"""
    autor: @erickgjs99
    file: practica_3.py
"""

datos = [1, 2 , 10, 11, 12, 13]

resultado = filter(lambda x: x % 2 == 0, datos)
print(list(resultado))