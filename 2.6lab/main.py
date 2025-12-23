from lines_module import line_from_points, are_parallel, point_on_line

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

A1, B1, C1 = line_from_points(x1, y1, x2, y2)
print("Уравнение первой прямой:", A1, "* x +", B1, "* y +", C1, "= 0")

x3 = float(input("Введите x3: "))
y3 = float(input("Введите y3: "))
x4 = float(input("Введите x4: "))
y4 = float(input("Введите y4: "))

A2, B2, C2 = line_from_points(x3, y3, x4, y4)
print("Уравнение второй прямой:", A2, "* x +", B2, "* y +", C2, "= 0")

print("Прямые параллельны:", are_parallel(A1, B1, C1, A2, B2, C2))

x = float(input("Введите x точки: "))
y = float(input("Введите y точки: "))
print("Точка принадлежит первой прямой:", point_on_line(x, y, A1, B1, C1))
