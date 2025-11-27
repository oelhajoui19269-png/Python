def sumar_llista(llista):
    suma = 0
    for num in llista:
        suma += num
    return suma

# Función para multiplicar todos los valores de una lista
def multiplicar_llista(llista):
    producte = 1
    for num in llista:
        producte *= num
    return producte

# Probamos las funciones con ejemplos
print(sumar_llista([1, 2, 3, 4]))        # 10
print(multiplicar_llista([1, 2, 3, 4]))  # 24
print(sumar_llista([5, 10, 15]))         # 30
print(multiplicar_llista([5, 10, 15]))   # 750