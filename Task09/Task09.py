# Задача №9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while.
# Пример:
# Input: 5
# Output: 120


number = int(input('Введите целое не отрицательное число '))
factorial = 1
if number > 0:
	count = 1
	while count <= number:
		factorial = factorial * count
		count = count + 1
	print(factorial)
else:
	print('Введите положительное целое число')