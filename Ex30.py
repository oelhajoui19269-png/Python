def binari_a_enter(binari):
    """
    Converteix una cadena binària a un enter.
    """
    try:
        return int(binari, 2)
    except ValueError:
        print("Error: La cadena no és un número binari vàlid.")
        return None

# Exemple d'ús
binari = input("Introdueix un número binari: ")
enter = binari_a_enter(binari)
if enter is not None:
    print(f"El número binari {binari} és l'enter {enter}")