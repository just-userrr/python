#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Эта программа считывает дискриминант, но только для мобильной версий. Эта программа тоже считывает неправильно, но зато красиво!
"""
from termcolor import colored # модуль для покраски текстов в терминале для красоты и читаемости
import math # для вычисления квадрат корня

print( "" ) # для отступа

# входные данные
a = int( input(colored( "a = ", 'white', attrs=['bold'] )) ) # введение нужных данных
b = int( input(colored( "b = ", 'white', attrs=['bold'] )) ) # введение нужных данных
c = int( input(colored( "c = ", 'white', attrs=['bold'] )) ) # введение нужных данных
print( "" ) # для отступа

# вычисление
d = b**2 - 4 * a * c # дискриминант
# вдруг словишь ValueError
try:
	x = (-b + math.sqrt(d)) // (2 * a) # х для случая, когда D = 0
	x1 = (-b + math.sqrt(d)) // (2 * a) # вычисление х1
	x2 = (-b - math.sqrt(d)) // (2 * a) # вычисление х2
except ValueError:
	print( colored( "Ошибка при вычислений дискриминанта! Проверьте, правильно ли вы написали данные!", 'red' ) ) # текст об ошибке
	print( "" ) # для отступа

# выходные данные
# вывод дискриминанта, вывод x1/2 дальше
# это для случая, если там есть цифры с отрицательным значением( - ), то программа берет его в скобку
if c < 0:
	print( colored( "D = " + str(b**2) + " - 4 * " + str(a) + " * ("  + str(c) + ") = "  + str(d), 'green', attrs=['bold'] ) )
elif a < 0:
	print( colored( "D = " + str(b**2) + " - 4 * (" + str(a) + ") * "  + str(c) + " = "  + str(d), 'green', attrs=['bold'] ) )
elif c < 0 and a < 0:
	print( colored( "D = " + str(b**2) + " - 4 * (" + str(a) + ") * ("  + str(c) + ") = "  + str(d), 'green', attrs=['bold'] ) )
elif c > 0 and a > 0:
	print( colored( "D = " + str(b**2) + " - 4 * " + str(a) + " * " + str(c) + " = " + str(d), 'green', attrs=['bold'] ) )
else:
	print( colored( "D = " + str(b**2) + " - 4 * " + str(a) + " * " + str(c) + " = " + str(d), 'green', attrs=['bold'] ) )
# вывод x1/2
if d < 0:
	print( colored( "Ответа нет!", 'red', attrs=['bold'] ) )
	print( "" )
elif d == 0:
	print( colored( "x1/2 = " + "(" + str(-b) + " +- " + str(math.sqrt(d))  + ") = " + str(x), 'green', attrs=['bold'] ) )
	print( "" )
elif d > 0:
	if x1 == x2:
		print( colored( "x1/2 = " + "(" + str(-b) + " +- " + str(math.sqrt(d)) + ") / (2 * " + str(a) + ") = " + str(x), 'green', attrs=['bold'] ) )
	else:
		print( colored( "x1/2 = " + "(" + str(-b) + " +- " + str(math.sqrt(d)) + ") / (2 * " + str(a) + ") = {" + str(x1) + "; " + str(x2) + "}", 'green', attrs=['bold'] ) )
print( "" ) # для отступа
