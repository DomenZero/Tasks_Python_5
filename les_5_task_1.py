'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за
четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''

from collections import OrderedDict
from collections import deque

def profit(mid_profit,all_profit):
    for i, item in companies.items():
        if item >= mid_profit:
            high_prof.append(i)
        else:
            low_prof.append(i)

n = int(input('Сколько предприятий: '))

companies=OrderedDict
profit_count=0
quart=4
all_profit=0
high_prof=deque()
low_prof=deque()


for i in range(n):
    name = input(f'\n Название компании № {i+1}: ')
    q=1
    while q <= quart:
        profit += float(input(f'Введите прибыль за {q} квартал: '))
        q+=1
    companies[name] = profit
    all_profit += profit


mid_profit = all_profit / n
profit(mid_profit,all_profit)
    
print(f'Средняя прибыль: {mid_profit}')
print(f'Прибыль выше среднего {len(high_prof)}:')
for name in high_prof:
    print(name)
print(f'Прибыль ниже среднего {len(low_prof)} :')
for name in low_prof:
    print(name)