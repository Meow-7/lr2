# . Дано ціле число, яке лежить в діапазоні 1-999. Вивести його рядок-опис виду «парне двозначне
# число», «непарне тризначне число» і т. Д.
x = int(input("enter the number = "))
if x > 999 or x < 1:
    print("x must be from 1 to 999")
    exit(0)


def number_description(x):
    if x % 2 == 0:
        print("парне")
    else:
        print("непарне")
    i = 0
    while x > 0:
        x = x//10
        i = i + 1
    print(i, "-Цифрове число")


number_description(x)
