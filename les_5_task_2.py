'''
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from collections import defaultdict
from collections import deque

dec_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
           'D': 13, 'E': 14, 'F': 15}


def to_dec(num):
    degree = 1
    num_dec = 0
    len_num = len(num)
    for i in num:
        if i in dec_num:
            i1 = 1
            degree = 1
            while i1 < len_num:
                degree = degree * 16
                i1 = i1 + 1
        num_dec = num_dec + dec_num[i] * degree

        len_num = len_num - 1
    return num_dec


def to_hex(num):
    deq = deque()
    deq_ost = deque()
    g = deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'])

    div_c = num // 16
    div = num % 16
    if num > 16:
        while div_c > 0:
            if div_c < 16 and div < 16:
                deq.append(g[div])
                deq.append(g[div_c])

            elif div < 16:
                deq.append(g[div])
            elif div_c < 16:
                deq.append(g[div_c])
            div = div_c % 16
            div_c = div_c // 16
    else:
        deq.appendleft(g[num])
    i = 0
    deq_all = deq_ost + deq
    deq_all.reverse()
    ll = list(deq_all)
    return ll


num1 = list(input('Введите первое hex число: '))
num2 = list(input('Введите второе hex число: '))

d = defaultdict(set)
num_dec1 = to_dec(num1)
num_dec2 = to_dec(num2)
sum_dec = num_dec1 + num_dec2
print(f'Сумма: {to_hex(sum_dec)}')
multi_dec = num_dec1 * num_dec2
print(f'Произведение: {to_hex(multi_dec)}')
