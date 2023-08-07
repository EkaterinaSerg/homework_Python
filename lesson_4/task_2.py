# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — хэш значения переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except Exception as t:
            print(t)
            result[str(value)] = key
    return result


print(kwargs_to_dict(username='Max', password='123', email='max@mail.ru'))
print(kwargs_to_dict(gadgets=['telephone', 'tablet', 'laptop']))
print(kwargs_to_dict(items={'ru': 'Русский', 'en': 'Английский'}))