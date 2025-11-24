def ex18(C):
    v = "aeiouAEIOUáàóòúùÀÁÈÉÓÒÚÙ"
    if c in v:
        return True
    else:
        return False
    
    # programa principal
    C= input("Escriu un caracter per a provar si es o no vocal:")
print(ex18(C))