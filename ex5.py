# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

rows = int(input("Введите количество рядов ёлки: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
