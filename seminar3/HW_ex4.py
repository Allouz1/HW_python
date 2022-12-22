w  # Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))
result = []

while number > 0:
    result.append(str(number % 2))
    number //= 2

print(''.join(result[::-1]))
