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
    pass