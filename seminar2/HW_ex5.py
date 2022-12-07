# Реализуйте алгоритм перемешивания списка.

from random import randint

def mix(lst):
    for i in range(len(lst)):
        new_i = randint(0, len(lst) - 1)
        lst[i], lst[new_i] = lst[new_i], lst[i]
        # tmp = lst[i]
        # lst[i] = lst[new_i]
        # lst[new_i] = tmp

lst_ = [1, 2, 3, 4, 5]
mix(lst_)
print(lst_)



# size = int(input('Размер списка: '))
# lst_2 = []

# for i in range(1, size + 1):
#     random.randint(1, size)
#     lst_2.append(random.randint(1, size))

# print(lst_2)

