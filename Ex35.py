def comptar_vocals(paraula):
    """
    Comptar el nombre de vegades que apareix cada vocal en una paraula.
    No diferencia majúscules de minúscules.
    Retorna un diccionari amb les vocals com a claus i la quantitat com a valors.
    """
    vocals = "aeiou"
    comptador = {v: 0 for v in vocals}

    for lletra in paraula.lower():
        if lletra in vocals:
            comptador[lletra] += 1

    return comptador


# Exemple 1
paraula1 = "Ratapinyada"
resultat1 = comptar_vocals(paraula1)
print(f"Paraula: {paraula1}")
for vocal, quantitat in resultat1.items():
    print(f"{vocal}: {quantitat}")
print()