#/usd/bin/env python
# -*- coding: utf-8 -*-
"""
Эта программа конвертер валют. Он может принять только USD и KZT.
"""
from termcolor import colored

print("")
option = int(input(colored( "Что хотите вычислить?:\n1) USD -> KZT;\n2) KZT -> USD\nВведите цифру варианта: ", 'white', attrs=['bold', 'dark'])))
print("")

if option == 1:
	usd = float(input(colored( "USD = ", 'white', attrs=['bold'] )))
	kzt = 404.3 # доллар в казахстанской тенге
	print(colored( str(usd) + "$", 'green', attrs=['bold', 'underline'] ) + " = " + colored( str(usd * kzt) + "₸", 'grey', 'on_green', attrs=['bold', 'dark', 'underline'] ))
elif option == 2:
	kzt = float(input(colored( "KZT = ", 'white', attrs=['bold'] )))
	usd = 0.0025 # тенге в американском долларе
	print(colored( str(kzt) + "₸", 'green', attrs=['bold', 'underline'] ) + " = " + colored( str(kzt * usd) + "$", 'grey', 'on_green', attrs=['bold', 'dark', 'underline'] ))
else:
	print(colored( "Вы неправильно ввели вариант!", 'red', attrs=['bold'] ))

print("")
