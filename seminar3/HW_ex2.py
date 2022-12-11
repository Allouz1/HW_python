# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]
new_lst = []
multi = 1

for i in range(len(lst)):
    num_first = lst[i]
    new_i = len(lst) - i - 1
    num_second = lst[new_i]
    if i <= 2:
        multi = num_first * num_second
        new_lst.append(multi)

print(new_lst)

