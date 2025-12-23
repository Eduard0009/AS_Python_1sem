file1 = open("1.txt", "r", encoding="utf-8")
file2 = open("2.txt", "r", encoding="utf-8")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

for i in range(len(lines1)):
    if i < len(lines2):
        lines1[i] = lines1[i].rstrip('\n') + lines2[i]

result = open("result.txt", "w", encoding="utf-8")
result.writelines(lines1)
result.close()

print("Готово. Результат записан в файл result.txt")
