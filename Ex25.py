def crear_punts(llista):
    for num in llista:
        print("." * num)

# Nueva función que dibuja una "imagen"
def dibuixar_imatge():
    # Definimos la "imagen" con una lista de números
    # Cada número indica cuántos puntos se dibujan en esa línea
    imatge = [1, 3, 5, 3, 1]
    crear_punts(imatge)

# Probamos la función
dibuixar_imatge()