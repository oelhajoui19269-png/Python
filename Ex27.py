def paraula_mes_llarga(llista_paraules):
    if not llista_paraules:  # Comprobamos si la lista está vacía
        return None
    paraula_llarga = llista_paraules[0]  # Empezamos suponiendo que la primera palabra es la más larga
    for paraula in llista_paraules:
        if len(paraula) > len(paraula_llarga):
            paraula_llarga = paraula  # Actualizamos si encontramos una palabra más larga
    return paraula_llarga

# Probamos la función
print(paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))  # "Paraula"
print(paraula_mes_llarga(["Python", "es", "genial"]))           # "Python"
print(paraula_mes_llarga(["a", "ab", "abc", "abcd"]))           # "abcd"
print(paraula_mes_llarga([]))                                   # None (lista vacía)