# Задача №11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что ?(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Пример:
# Input: 5
# Output: 6


number = int(input('Введите число Фибоначчи '))

firstfib = 0
secondfib = 1
tempfib = firstfib + secondfib
index = 2

while tempfib < number:
	firstfib = secondfib
	secondfib = tempfib
	tempfib = firstfib + secondfib
	index = index + 1
if tempfib == number:
	print(index + 1)
else:
	print(-1)