def nums_que_comencen_per(llista_noms):
    comptador = 0
    for nom in llista_noms:
        if nom.startswith('a'):
            comptador += 1
    return comptador
