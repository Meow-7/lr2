from math import*
# Для даного дійсного x знайти значення наступної функції f, що приймає дійсні значення:
# f (x) = 2 • sin (x), якщо x> 0; 6 - x, якщо x ≤ 0.
x = int(input("enter the number = "))


def function(x):
    if x > 0:
        f = 2*sin(x)
        print(f)
    else:
        f = 6 - x
        print(f)
    return f


function(x)
