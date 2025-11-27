def gran_llista(llista):
    if not llista:  # Comprobamos si la lista está vacía
        return None
    max_num = llista[0]  # Empezamos suponiendo que el primer número es el mayor
    for num in llista:
        if num > max_num:
            max_num = num  # Actualizamos si encontramos un número mayor
    return max_num

# Probamos la función
print(gran_llista([3, 4, 2, 3, 10]))  # 10
print(gran_llista([7, 1, 5, 9, 2]))   # 9
print(gran_llista([-3, -7, -1, -5]))  # -1
print(gran_llista([]))                # None (lista vacía)