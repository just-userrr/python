#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Эта программа выводит оценки по СОР/СОЧ
"""
from colorama import Fore, Back, Style, init
init()

print( "\033[1m\033[37m" )

# максимальный балл
mball = int(input( "Максимальный балл: " ))

# баллы, которую я получил
tball = int(input( "Сколько ты получил баллов: " ))
print( "" )

# вычисление
result = (tball * 100) / mball

# выходные данные
result_text = "Ты получил " + str( int(result) ) + " процентов"
# итоговые оценки
if result >= 85 and result <= 100:
	print( "\033[2m\033[32m{}".format( result_text ) )
	print( "\033[2m\033[32m{}".format( "Оценка: 5" ) )
elif result > 64 and result <= 84:
	print( "\033[1m\033[32m{}".format( result_text ) )
	print( "Оценка: 4" )
elif result > 40 and result <= 64:
	print( "\033[1m\033[33m{}".format( result_text ) )
	print( "Оценка: 3" )
elif result >= 1 and result <= 39:
	print( "\033[1m\033[31m{}".format( result_text ) )
	print( "Оценка: 2" )

# на случай, если данные были введены неверно
if result > 100:
	print( "\033[1m\033[31m{}".format("Значение написано неправильно!") )
elif result < 0:
	print( "\033[1m\033[31m{}".format("Значение написано неправильно!") )
elif result == 0:
	print( "\033[1m\033[31m{}".format("Значение написано неправильно!") )

print( Style.RESET_ALL + Fore.RESET )
