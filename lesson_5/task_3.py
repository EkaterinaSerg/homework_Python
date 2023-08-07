# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fib(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    number = int(input('Enter the number of elements: '))
    print(list(fib(number)))

