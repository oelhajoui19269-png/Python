def superposicio(llista1, llista2):
    # Recorremos los elementos de la primera lista
    for element in llista1:
        if element in llista2:  # Si el elemento está en la segunda lista
            return True
    return False  # Si no hay elementos en común

# Probamos la función
print(superposicio([1, 2, 3], [3, 4, 5]))   # True (3 está en ambas)
print(superposicio([1, 2, 3], [4, 5, 6]))   # False (no hay elementos comunes)
print(superposicio(['a', 'b'], ['c', 'b'])) # True (b está en ambas)
print(superposicio([], [1, 2]))             # False (lista vacía)
