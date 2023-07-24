# Решите квадратное уравнение 5x2 #-10x-400=0 последовательно сохраняя переменные a, b, c, d, x1 и x2

a = float(input("Введите а = "))
b = float(input("Введите b = "))
c = float(input("Введите c = "))
print("Решим уравнение: {}x^2 + {}x + {} = 0".format(a, b, c))
if a == 0:
    if b == 0:
        if c == 0:
            print("Корней бесконечно много")
        else:
            print("Нет решений")
    else:
        x1 = -c / b
        print("x1 = ", x1)
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print("x1 = ", x1, "\n", "x2 = ", x2)
elif discriminant == 0:
    x1 = -b / (2 * a)
else:
    print("Нет решений")
