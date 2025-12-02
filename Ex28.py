def filtrar_paraules(llista, x):
    """
    Retorna totes les paraules de 'llista' que tinguin més de x caràcters.
    """
    return [paraula for paraula in llista if len(paraula) > x]