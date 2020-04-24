#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Autor: Erasyl_Seralyuly

Version: 2.0

This programm counts discriminant
"""
print("") # для отступа

import os
# автоматическая установка всех необходимых модулей
os.system('pip3 install termcolor')
os.system('pip3 install colorama')

from termcolor import colored
from colorama import Fore, Back, Style
import math

# входные данные
a = int(input( Back.YELLOW + Fore.BLACK + "Введите а: " ))
b = int(input( Back.YELLOW + Fore.BLACK + "Введите b: " ))
c = int(input( Back.YELLOW + Fore.BLACK + "Введите c: " ))
print(Style.RESET_ALL)

# вычисление
d = b**2 - 4 * a * c

try:
	x = (-b + math.sqrt(d)) // (2 * a) 
	x1 = (-b + math.sqrt(d)) // (2 * a)
	x2 = (-b - math.sqrt(d)) // (2 * a)
except ValueError:
	print( Fore.BLACK + Back.RED + "Ошибка при вычислений дискриминанта! Проверьте, правильно ли вы написали данные!" )
	print(Style.RESET_ALL)

# выходные данные
# дискриминант
if c < 0:
	print( Fore.BLACK + Back.GREEN + "D = " + str(b**2) + " - 4 * " + str(a) + " * ("  + str(c) + ") = "  + str(d) )
elif a < 0:
	print( Fore.BLACK + Back.GREEN + "D = " + str(b**2) + " - 4 * (" + str(a) + ") * "  + str(c) + " = "  + str(d) )
elif c < 0 and a < 0:
	print( Fore.BLACK + Back.GREEN + "D = " + str(b**2) + " - 4 * (" + str(a) + ") * ("  + str(c) + ") = "  + str(d) )
elif c > 0 and a > 0:
	print( Fore.BLACK + Back.GREEN + "D = " + str(b**2) + " - 4 * " + str(a) + " * " + str(c) + " = " + str(d) )
else:
	print( Fore.BLACK + Back.GREEN + "D = " + str(b**2) + " - 4 * " + str(a) + " * " + str(c) + " = " + str(d) + Style.RESET_ALL)
# x1/2
if d < 0:
	print( Fore.BLACK + Back.RED + "Ответа нет!" )
	print(Style.RESET_ALL)
elif d == 0:
	print( Fore.BLACK + Back.RED + "x1/2 = " + "(" + str(-b) + " +- " + str(math.sqrt(d))  + ") = " + str(x) )
	print(Style.RESET_ALL)
elif d > 0:
	if x1 == x2:
		print( Fore.BLACK + Back.GREEN + "x1/2 = " + "(" + str(-b) + " +- " + str(math.sqrt(d)) + ") / (2 * " + str(a) + ") = " + str(x) )
	else:
		print( Fore.BLACK + Back.GREEN + "x1/2 = " + "(" + str(-b) + " +- " + str(math.sqrt(d)) + ") / (2 * " + str(a) + ") = {" + str(x1) + "; " + str(x2) + "}" )
print(Style.RESET_ALL)

