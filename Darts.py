from math import sqrt

def score(x, y):
    radious = sqrt(x**2 + y**2)
    if radious > 10:
        return 0
    elif radious > 5:
        return 1
    elif radious > 1:
        return 5
    else:
        return 10

print("Ingrese las cordenadas del dardo para descubrir su puntaje")    

cordenada1 = int(input("Ingrese la Cordenada 1: "))
cordenada2 = int(input("Ingrese la Cordenada 2: "))

print("Puntos: ", score(cordenada1, cordenada2))