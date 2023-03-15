# 1 Вводятся числа, пока не введется 0. Найти сумму чисел кратных 3

summa = 0

while True:
    number = int(input('Введите числа'))
    if number == 0:
        break
    elif number % 3 == 0:
        summa = summa + number
print(summa)
