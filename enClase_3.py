"""
    autor: @erickgjs99
    file:  enClase_3.py
    Dadas las siguiente ciudades, filtrar aquellas que tienen un número par como longitud en sus caracteres.
    Loja, Pichincha, Guayaquil, Zamora, Ibarra, Manabi, Machala,  Portoviejo, Macas
"""
ciudades = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", "Machala", "Portoviejo", "Macas"]

verif = filter(lambda x: len(x) % 2 == 0, ciudades)

print(list(verif))