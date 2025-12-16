import random

def generar_codi():
    """Genera un codi aleatori de 4 xifres com a llista."""
    return [random.randint(0, 9) for _ in range(4)]

def comprovar_jugada(codi_secret, jugada):
    """
    Retorna dos valors:
    - encerts: números correctes en la posició correcta
    - coincidencies: números correctes però en posició incorrecta
    """
    encerts = 0
    coincidencies = 0
    
    codi_secret_copy = codi_secret.copy()
    jugada_copy = jugada.copy()
    
    # Primer, comptar encerts (mateixa posició)
    for i in range(4):
        if jugada_copy[i] == codi_secret_copy[i]:
            encerts += 1
            codi_secret_copy[i] = jugada_copy[i] = None  # Marcar com comptat
    
    # Després, comptar coincidències (mateix número, posició diferent)
    for i in range(4):
        if jugada_copy[i] is not None and jugada_copy[i] in codi_secret_copy:
            coincidencies += 1
            codi_secret_copy[codi_secret_copy.index(jugada_copy[i])] = None

    return encerts, coincidencies

# --- Programa principal ---
print("Benvingut al MasterMind simplificat!")
print("Introdueix codis de 4 xifres fins a endevinar el codi secret.")

codi_secret = generar_codi()
intents = 0

while True:
    entrada = input("Introdueix un codi de 4 xifres: ")
    
    if len(entrada) != 4 or not entrada.isdigit():
        print("Error: el codi ha de tenir exactament 4 xifres.")
        continue
    
    jugada = [int(x) for x in entrada]
    intents += 1
    
    encerts, coincidencies = comprovar_jugada(codi_secret, jugada)
    
    if encerts == 4:
        print(f"Enhorabona! Has endevinat el codi en {intents} intents!")
        break
    else:
        print(f"Encerts: {encerts}, Coincidències: {coincidencies}")