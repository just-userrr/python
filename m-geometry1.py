#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Erasyl_Seralyuly

Version: 1.0

Эта программа выведет координаты середины прямой линий
"""
from termcolor import colored

# входные данные
print( "" ) # для отступа
x1 = float( input(colored( "x1 = ", 'white', attrs=['bold'] )) ) # X координата первой точки
y1 = float( input(colored( "y1 = ", 'white', attrs=['bold'] )) ) # Y координата первой точки
x2 = float( input(colored( "x2 = ", 'white', attrs=['bold'] )) ) # X координата второй точки
y2 = float( input(colored( "y2 = ", 'white', attrs=['bold'] )) ) # Y координата второй точки
print( "" ) # для отступа

# вычисление координат нужной точки
x = (x1 + x2) / 2 # X координата середины прямой
y = (y1 + y2) / 2 # Y координата середины прямой

# выходные данные
print( colored( "C(" + str(x) + "; " + str(y) + ")", 'green', attrs=['bold'] ) ) # оконочательные координаты середины
print( "" ) # для отступа
