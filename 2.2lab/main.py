import math

def RingS(R1, R2):
    return math.pi * (R2**2 - R1**2)

R1 = float(input("Введите внутренний радиус R1: "))
R2 = float(input("Введите внешний радиус R2: "))

S = RingS(R1, R2)
print("Площадь кольца:", S)
