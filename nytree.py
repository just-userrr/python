import math
import random
from termcolor import colored, cprint

# правильные пропорции должны быть 1:2, например row = 25, col = 50
row = 30
col = 60 # лучше это вводить в четных числах (жұп сандар), а так лищний символ наверху можно replace-нуть в горящую звезду (если это четное число, то replace)
now = 0

n = math.floor(col/2)
# print(n)
m = math.floor(row / n)
# print(m)

j = m
if row / n != row // n:
        j += 1 # j = 1

o = 0
l = 0

cprint(' '*n + '**', "yellow", attrs=["bold", "blink"])
for i in range(now, row):
    s = ' '*n + '*' + '*'*o + '*'
    #light = colored('o', "blue", attrs=["bold", "blink"])
    light = 'o'

    num_of_index = random.randint(0, l/2) # сколько элементов в строке заменятся
    random_index_list = [random.randint(n, n+l+1) for j in range(num_of_index)] # список индексов для букв в строке, которые заменятся

    # print(sorted(random_index_list))
    
    for u in random_index_list:
        if u == u+1:
            random_index_list.pop(u+1)
    
    # print(sorted(random_index_list))

    for y in random_index_list:
        s = s[:y] + light + s[y+1:]
        s[:n].replace('o', ' ')
    cprint(s, "green")
    if i == j-1:
        n -= 1
        o += 2
        j += m
    l += 2



n = math.floor(col/2)
p = 1
if row > 10 and row <= 20:
    p = 2
elif row > 20 and row <= 30:
    p = 3
for k in range(p):
    cprint(' '*n + '||', "red", attrs=["dark"])
# print(n)
