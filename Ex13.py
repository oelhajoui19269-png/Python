def menu_principal():
    opcio=0
    while opcio<1 or opcio>4:
        opcio=int(input("""Elegeix una opcio:
                    1. calculadora decimal
                    2. calculadora real (floats)
                    3. Canvis de base
                    4. sortir"""))
        if opcio>0 and opcio<4:
            return opcio
        else:
            print("L'opcio seleccionada no és correcte, torni-ho a provar !!\n")
def menu_calculadora():
     opcio=0 
     while opcio<1 or opcio>5:
        opcio =int(input("""Elegeixi una opció: 
                1. Suma
                2. Resta
                3. Muliplicació
                4. Divisió
                0. Sotir
                """))
        if opcio>0 and opcio<6:
            return opcio
        else:
            print("L'opcio seleccionada no és corecte,torni-ho provar!!\n")
    
def Calculadora_decimal(opcio):
    if opcio>0 and opcio<5:
        a = int(input("Introdueixi el primer numero:"))
        b = int(input("Introdueixi el segon numero:"))
    match(opcio):
        case 1:
            # suma
            print("estic fent suma! \n")
            c = a + b
            print("El resultat de sumar {} + {} és {}" .format(a, b, c))
        case 2:
            # resta
            print("estic fent resta! \n")
            c = a - b
            print("El resultat de sumar {} - {} és {}" .format(a, b, c))
        case 3:
            # multiplicació
            print("estic fent multiplicación! \n")
            c = a * b
            print("El resultat de sumar {} * {} és {}" .format(a, b, c))
        case 4:
            # división
            print("estic fent la divisió! \n")
            c = a // b
            print("El resultat de sumar {} // {} és {}" .format(a, b, c))
        case __:
            print("opcio no  válida! Torni-ho a provar!!\n")
def calculadora_real():
    if opcio>0 and opcio<5:
        a = float(input("Introdueixi el primer numero:"))
        b = float(input("Introdueixi el segon numero:"))
    match(opcio):
        case 1:
            # suma
            print("estic fent suma! \n")
            c = a + b
            print("El resultat de sumar {} + {} és {}" .format(a, b, c))
        case 2:
            # resta
            print("estic fent resta! \n")
            c = a - b
            print("El resultat de sumar {} - {} és {}" .format(a, b, c))
        case 3:
            # multiplicació
            print("estic fent multiplicación! \n")
            c = a * b
            print("El resultat de sumar {} * {} és {}" .format(a, b, c))
        case 4:
            # división
            print("estic fent la divisió! \n")
            c = a // b
            print("El resultat de sumar {} // {} és {}" .format(a, b, c))
        case __:
            print("opcio no  válida! Torni-ho a provar!!\n")   

# Peogrma principal
op = 1
while   op != 0:
    op = menu_principal()
    if op==1:
        # calculadora decimal
        print("Estic passant per la calculadora decimal!\n")
        calculadora_decimal(menu_calculadora())
    elif op==2:
        #Calculadora real
        print("Estic passant per la calculadora decireal mal!\n")
        calculadora_real (menu_calculadora())
    else:
        print("Gràcies per utilitzar la meva calculadora, fins un altre dia! \n")
        op=0
        #Canvis de base
        print("Estic pasant per canvis de base!\n")
        print("Gràcies per utilitzar la meva calculadora, fins un altre dia! \n")
        op=0