def es_palindrom(paraula):
    # Convertimos la palabra a minúsculas para que no importe mayúsculas/minúsculas
    paraula = paraula.lower()
    # Comparamos la palabra con su versión invertida
    return paraula == paraula[::-1]

# Probamos la función con distintos ejemplos
print(es_palindrom("radar"))   # True
print(es_palindrom("ara"))     # True
print(es_palindrom("civic"))   # True
print(es_palindrom("rallar"))  # True
print(es_palindrom("tapat"))   # True
print(es_palindrom("simis"))   # True
print(es_palindrom("refer"))   # True
print(es_palindrom("python"))  # False