def mostrar_majors_que(tupla_nums, x):
    """
    Mostra tots els números de la tupla que són majors que x.
    """
    for num in tupla_nums:
        if num > x:
            print(num, end=' ')
    print()  # per salt de línia final

# Programa principal per provar la funció
# Demanar els valors de la tupla
valors = input("Introdueix els nombres enters separats per espais: ")
tupla_nums = tuple(int(n) for n in valors.split())

# Mostrar els que són majors de 18
print("Els números majors de 18 són:")
mostrar_majors_que(tupla_nums, 18)
