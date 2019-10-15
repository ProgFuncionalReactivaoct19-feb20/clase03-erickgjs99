"""
    autor: @erickgjs99
    file:  enClase.py
    dado un conjunto de palabras filtrar todas aquellas que sean palindromas
"""

word = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]


w_alreves = filter(lambda x: "".join(reversed(x)) == x, word)


print(list(w_alreves))