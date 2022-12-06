# Реализуйте алгоритм перемешивания списка.

import random


size = int(input('Размер списка: '))
lst_2 = []

for i in range(1, size + 1):
    random.randint(1, size)
    lst_2.append(random.randint(1, size))

print(lst_2)

