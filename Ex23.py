def crear_repetits(n, caracter):
    return caracter * n

# Probamos la función
print(crear_repetits(5, "a"))   # "aaaaa"
print(crear_repetits(3, "x"))   # "xxx"
print(crear_repetits(0, "b"))   # "" (cadena vacía)
print(crear_repetits(7, "*"))   # "*******"