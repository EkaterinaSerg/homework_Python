# Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def main(names_list, rates_list, premium_list):
    return {name: rate * (1 + float(prem.strip('%'))) for name, rate, prem in zip(names_list, rates_list, premium_list)}


if __name__ == '__main__':
    names = ['First', 'Second', 'Third']
    rates = [1.5, 1, 2]
    premium = ['14.17%', '10.25%', '7.05%']
    print(main(names, rates, premium))

