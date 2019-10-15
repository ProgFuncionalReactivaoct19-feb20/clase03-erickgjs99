"""
    autor: @erickgjs99
    file: practica_4.py
"""

datos = [18, 19, 20, 10, 11, 12]

resultado = filter(lambda x: x >= 18 or x <= 10, datos)
print(list(resultado))