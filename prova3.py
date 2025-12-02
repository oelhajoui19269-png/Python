
















"""

def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return 1
    #programa principal
a = int(input("Introdueixi un numero per a a fer el factorial"))
print(factorial(a))


def sumaun(m):
    for i,e in enumerate(l):
        m[i]=e + 1

#programa principal
l=[5, 6, 7, 10]
print(l)
sumaun(l)
print(l)


# Ordenar 
# llegir 2 nombre
# imprimir tots el nombres entre el menor y el major
def ordenar(x, y):
        # prec: donat dos numeros
        # post: retorna el major i menor

        if x>y:
                return y, x
        elif y>x:
                return y, x
        else:
                return x, y
   #programa principal     
v1 = int(input("Intro el 1r numero: "))
v2 = int(input("Intro el 2n numero ")) 
v2, v1 = ordenar(v1, v2)
for e in range(v2, v1+1):
         if e %2==0:
                 print(e) 
"""


# Llegir 2 nombres
"""v1 = int(input("Intro el 1r numero: "))
v2 = int(input("Intro el 2n numero"))
# multipolcar i dividir per 2
r  = (v1*v2)//2
# implimentar el numero 0
for i in range(r, 0, -1):
    print(i)
    """



"""v1 = int(input("Intro el 1r numero: "))
v2 = int(input("Intro el 2n numero"))
r  = v1*v2
if (r>=45 and r<=35)or(r>=105 and r<=125):
        print("A")
elif    (r>=45  and r<=65) or (r>=145 and r<=165):
        print("B")
else:
        print("C")
        """




"""
a.append(10)
a.append("Cadena nova")
a.append([10, 11, 12])
print(a.sort())

# pasant elementes de la lista a string
for i in range(len(a)):
    a[i]=str(a[i])
print(str(a))
# crea un unic string 
print("".join(a))


for i in range(len(a)):
    a[i]=str(a[i])
print(a.sort())
b = a.copy()
b[0]=100
print(a)

print(a[::-1]) # retorna un allista invertida pero no modificada l'original
print(a)
print(a.reverse()) # no retorna res, pero modifica l allista original
print(a)
"""
""""
a.extend([10, "Cadena nova", [10, 11, 12]])
print(a)
"""
"""
for e in a:
        print(e)
for i in  range(len(a)):
        a[i]*=2 # --> a [i]= a [i]*2
        print("LA posicio {} te el valor {}".format(i,a[i]))
for i,e in enumerate(a):
        print ("LA posicio {} te el valor {}".format(i,e))
"""
