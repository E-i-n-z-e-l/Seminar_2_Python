# Задача №15.  Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.

# Пример:
# Input: 5 -> 5 1 6 5 9
# Output: 1 9



watermelons = int(input('Введите кол-во арбузов '))

bigwatermelons = 0
minwatermelons = 0

for i in range(watermelons):
	watermelons_weight = int(input('Введите вес арбуза '))
	while watermelons_weight <= 0 or watermelons_weight > 30000:
		print('Задайте другой вес арбуза ')
		watermelons_weight = int(input('Введите вес арбуза '))
	if i == 0:
		minwatermelons = watermelons_weight
		bigwatermelons = watermelons_weight
	if i != 0:
		if watermelons_weight > bigwatermelons and watermelons_weight < 30000:
			bigwatermelons = watermelons_weight
		if watermelons_weight < minwatermelons and watermelons_weight > 0:
			minwatermelons = watermelons_weight

print(f'Арбуз для Ивана Васильевича {bigwatermelons} ')
print(f'Арбуз для тещи {minwatermelons} ')