def leap_year(year):
    return year%4 ==0 and (year%100!=0  or year%400==0)
    

anno = int(input("Ingrese un año: "))

print("El año {} es bisiesto?".format(anno))

print(leap_year(anno))