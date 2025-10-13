import math

a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
angle = float(input("Введите угол между ними в градусах: "))

angle_rad = math.radians(angle)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle_rad))

print("Длина третьей стороны: ", c)