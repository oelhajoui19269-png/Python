def nums_que_comencen_per(llista_noms, lletra):
    """
    Retorna el nombre d'elements de la llista que comencen per la lletra especificada.
    La comprovació no diferencia majúscules de minúscules.
    """
    comptador = 0
    for nom in llista_noms:
        if nom.lower().startswith(lletra.lower()):
            comptador += 1
    return comptador

# Exemple d'ús
noms = ["Anna", "Albert", "Aina", "Joan", "Abel"]

# Demanem a l'usuari la lletra
lletra = input("Introdueix una lletra: ")

# Comptem i mostrem el resultat
resultat = nums_que_comencen_per(noms, lletra)
print(f"Noms que comencen per '{lletra}': {resultat}")
