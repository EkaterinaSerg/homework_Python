# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

num = int(input('Enter a number: '))

print(hex(num))

MOD = 16
list_1 = []

while num != 0:
    last_digit = num % MOD
    if last_digit == 10:
        last_digit = 'a'
    elif last_digit == 11:
        last_digit = 'b'
    elif last_digit == 12:
        last_digit = 'c'
    elif last_digit == 13:
        last_digit = 'd'
    elif last_digit == 14:
        last_digit = 'e'
    elif last_digit == 15:
        last_digit = 'f'
    list_1.append(last_digit)
    num //= MOD
list_1.reverse()

print('0x', *list_1, sep='')
