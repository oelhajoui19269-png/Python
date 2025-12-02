def comptar_majuscules(cadena):
    """
    Retorna el nombre de lletres majúscules en la cadena.
    """
    return sum(1 for c in cadena if c.isupper())
print(comptar_majuscules("Hola Món"))            # 2
print(comptar_majuscules("python"))              # 0
print(comptar_majuscules("Això És UNA Prova"))   # 6
print(comptar_majuscules("123ABCdef!"))          # 3
