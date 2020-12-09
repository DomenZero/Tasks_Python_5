'''
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from collections import defaultdict
from collections import deque

dec_num={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}


def sum_hex():
    print()

def multi_hex():
    print()

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
    deq_ost=deque()
    # g = deque()
    g = deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'])
    print(g.index(1))
    if num > 16:
        div = num % 16
        div_c = num // 16
        deq_ost.append(div_c)
        if div < 16:
            deq.appendleft(div)
        else:
            while div > 16:
                div = num % 16
            if div in dec_num:
                print(dec_num[div])
            deq.appendleft(div)

    i=0
    print()
    for i in deq:
        print(deq[i])

num1 = list(input('Введите первое hex число: '))
num2 = list(input('Введите второе hex число: '))

d=defaultdict(set)
num_dec1=to_dec(num1)
print(num_dec1)
num_dec2=to_dec(num2)
print(num_dec2)
num_dec=num_dec1+num_dec2
print(num_dec)
to_hex(num_dec)

print(num1)
print(num2)



