# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 10) многочлена и записать как многочлен степени k.
#  Пример:
#
#  k=2  - это максимальная степень многочлена, то есть в данном случае будет x2
#  - > 2*x² + 4*x + 5 = 0  при списке [2 ,4 ,5 ]
#        или  x² + 5 = 0   при списке [1 ,0 ,5 ]
#        или  10*x² = 0   при списке [10 ,0 ,0 ]
# k=3 - > 5*x^3 + 6*x^2 + 7*x + 10 = 0 при списке [ 5 , 6 , 7, 10]

from random import randint

k = int(input('Enter k: '))
lst = [randint(0, 10) for i in range(k + 1)]
print(lst)

mnozh = []
for i in range(len(lst)):
    if lst[i] != 0:
        if k - i > 1:
            element = f'{lst[i]}*x^{k - i}'
        elif k - i == 1:
            element = f'{lst[i]}*x'
        else:
            element = f'{lst[i]}'
        mnozh.append(element)
# print(mnozh)

the_equation = ' + '.join(mnozh)
print(f'{the_equation} = 0')
