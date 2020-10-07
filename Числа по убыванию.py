numbers = []
for i in range(int(input("Введите количество чисел:"))):
	numbers.append(int(input("Введите числа:")))
print(list(reversed(sorted(numbers))))