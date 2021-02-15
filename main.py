import math

def first(x):
    y = (x**5/78-21*x**3)**0.5 + 2*x**8 + 21*x**7 + (51*x**7 + x**3)/(x**8 + math.cos(x) - 3)
    return y
print("Задача 1.1. Реализовать функцию")
print ("f(57) = {:.2e}".format(first(57)))
print ("f(94) = {:.2e}".format(first(94)))
print()

def second(x):
    if x < -8:
        return x**5/59 - 34*x**3
    elif (-8 <= x) and (x < 36):
        return 2*x**4 + math.exp(x)
    elif x >= 36:
        return 66*x**2 - x**6
    else : print("Error")
print("Задача 1.2. Реализовать кусочно­линейную функцию")
print ("f(-24) = {:.2e}".format(second(-24)))
print ("f(25) = {:.2e}".format(second(25)))
print()

def third(n, m):
    return 36*fu1(n) + 45*fu2(n, m)
def fu1(n):
    summ = 0
    for i in range(1, n+1):
        summ += i**5/78 - 21*i**3
    return summ
def fu2(n, m):
    summ = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            summ += 99*i**8 - 52*i + 13
    return summ
print("Задача 1.3. Реализовать итерационную функцию")
print ("f(70, 95) = {:.2e}".format(third(70, 95)))
print ("f(36, 27) = {:.2e}".format(third(36, 27)))
print()

def fourth(n):
    if n == 0:
        return 3
    return math.sin(float(fourth(n - 1))) + (1/72)*float((fourth(n-1)))**3
print("Задача 1.4. Реализовать рекуррентную функцию")
print ("f(8) = {:.2e}".format(fourth(8)))
print ("f(9) = {:.2e}".format(fourth(9)))