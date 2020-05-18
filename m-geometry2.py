#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Erasyl_Seralyuly

Version: 1.0

Эта программа выведет координаты точки прямого (не центр прямого)
"""
from termcolor import colored

# входные данные
print( "" ) # для отступа
A1A = int(input( colored( "A1A = ", 'white', attrs=['bold'] ) )) # соотношение первого отрезка ко второму
AA2 = int(input( colored( "AA2 = ", 'white', attrs=['bold'] ) )) # соотношение второго отрезка к первому
x1 = float(input( colored( "x1 = ", 'white', attrs=['bold'] ) )) # X координата первой головы
y1 = float(input( colored( "y1 = ", 'white', attrs=['bold'] ) )) # Y координата первой головы
x2 = float(input( colored( "x2 = ", 'white', attrs=['bold'] ) )) # X координата второй головы
y2 = float(input( colored( "y2 = ", 'white', attrs=['bold'] ) )) # Y координата второй головы
print( "" ) # для отступа

# вычисление
L = A1A // AA2 # лямбда
x = ( x1 + L * x2 ) // ( 1 + L ) # X координата нужной точки
y = ( y1 + L * y2 ) // ( 1 + L ) # Y координата нужной точки

# выходные данные
print( "" ) # для отступа
print( colored( "L = " + str(A1A) + "/" + str(AA2), 'green', attrs=['bold'] ) ) # лямбда
print( colored( "x = " + "(" + str(x1) + " + (" + str(A1A) + "/" + str(AA2) + ") * " + str(x2) + ") / (1 + (" + str(A1A) + "/" + str(AA2) + ")) = " + str(x), 'green', attrs=['bold'] ) ) # X координата нужной точки
print( colored( "y = " + "(" + str(y1) + " + (" + str(A1A) + "/" + str(AA2) + ") * " + str(y2) + ") / (1 + (" + str(A1A) + "/" + str(AA2) + ")) = " + str(y), 'green', attrs=['bold'] ) ) # Y координата нужной точки
print( colored( "C(" + str(x) + "; " + str(y) + ")", 'grey', 'on_green', attrs=['bold'] ) ) # окончательные координаты нужной точки
print( "" ) # для отступа
