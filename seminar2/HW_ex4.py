# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

n = int(input('Введите число N:'))
a = int(input('Позиция 1:'))
b = int(input('Позиция 2:'))
lst = []

for num in range(-n, n + 1):
    lst.append(num)

print(lst[a])
print(lst[b])
sum = lst[a] *lst[b]
print(lst)
print(sum)
