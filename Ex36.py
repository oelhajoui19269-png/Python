def es_de_traspas(any):
    """
    Retorna True si l'any és de traspàs, False en cas contrari.
    Un any és de traspàs si:
    - És divisible per 4 i no divisible per 100, o
    - És divisible per 400
    """
    return (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0)


# Exemple d'ús
anys = [1900, 2000, 2024, 2023]

for any in anys:
    if es_de_traspas(any):
        print(f"L'any {any} és de traspàs.")
    else:
        print(f"L'any {any} no és de traspàs.")