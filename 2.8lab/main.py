file = open("f.txt", "r", encoding="utf-8")

numbers = []
for line in file:
    numbers.append(float(line))

file.close()

min_value = numbers[0]
max_value = numbers[0]

for num in numbers:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

result = min_value + max_value

print("Сумма макс и мин:", result)
