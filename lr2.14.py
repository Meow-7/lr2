# Дано три різних числа. Знайти, яке з них є середнім (більше одного, але менше іншого)
x = int(input("enter the number"))
y = int(input("enter the number"))
z = int(input("enter the number"))


def find_middle(x, y, z):
    if x > y:
        max = x
        if z > max:
            max = z
            if x > y:
                print("x is middle")
            else:
                print("y is middle")
        else:
            if z > y:
                print("z is middle")
            else:
                print("y is middle")


    else:
        max = y
        if z > max:
            max = z
            if x > y:
                print("x is middle")
            else:
                print("y is middle")
        else:
            if x > z:
                print("x is middle")
            else:
                print("z is middle")


find_middle(x, y, z)
