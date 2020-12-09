'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за
четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''

from collections import namedtuple

n = int(input('Сколько предприятий: '))
New_Company = namedtuple('New_Company', 'name,profit1,profit2,profit3,profit4')

all_companies = set()
all_profits = set()
profit_count = 0
all_profit = 0

for i in range(n):
    name = input(f'\n Название компании № {i + 1}: ')
    profit1 = float(input(f'Введите прибыль за 1 квартал: '))
    profit2 = float(input(f'Введите прибыль за 2 квартал: '))
    profit3 = float(input(f'Введите прибыль за 3 квартал: '))
    profit4 = float(input(f'Введите прибыль за 4 квартал: '))
    company = New_Company(name=name, profit1=profit1, profit2=profit2, profit3=profit3, profit4=profit4)
    all_companies.add(company)
    all_profit += profit1 + profit2 + profit3 + profit4
    all_profits.add(all_profit)

mid_profit = all_profit / n

print(f'Средняя прибыль: {mid_profit}')
print(f'Прибыль выше среднего:')
for company in all_companies:
    if int(company.profit1 + company.profit2 + company.profit3 + company.profit4) > mid_profit:
        print(
            f'Компания {company.name} зарплата = {company.profit1 + company.profit2 + company.profit3 + company.profit4}')
print(f'Прибыль ниже среднего:')
for company in all_companies:
    if int(company.profit1 + company.profit2 + company.profit3 + company.profit4) < mid_profit:
        print(
            f'Компания {company.name} зарплата = {company.profit1 + company.profit2 + company.profit3 + company.profit4}')
