#2 Найти сумму цифр числа

number = int(input('Введите число'))
summa = 0
while number > 0:
	summa = summa + (number % 10)
	number = number // 10
print(summa)