# Demanar l'any actual
any_actual = int(input("Introdueix l'any actual: "))

# Llista per guardar les dades de les persones
persones = []

# Recollir dades de 4 persones
for i in range(4):
    nom = input(f"Introdueix el nom de la persona {i+1}: ")
    any_naixement = int(input(f"Introdueix l'any de naixement de {nom}: "))
    persones.append((nom, any_naixement))

# Imprimir la taula
print("\nNom\t\tData naixement\tAnys que farà aquest any")
for nom, any_naixement in persones:
    edat = any_actual - any_naixement
    print(f"{nom}\t\t{any_naixement}\t\t{edat}")