#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Эта программа выведет итог четверти
Напиши команду 'help' без кавычек в первой же строке, и ты получишь инструкцию по этой программе!
"""
from termcolor import colored

#====================================================================================================

# входные данные

#====================================================================================================
# 1-четверть
print("\n") # для отступа
print(colored( "1-четверть: ", 'cyan', attrs=['bold'] ))
# макс. баллы по СОР/СОЧ
msor1_1s = input(colored( "Макс. балл СОР№1: ", 'white', attrs=['bold'] ))

# для получения помощи
help_msg = "Привет! Это краткая инструкция по этой программе! Зайди в EduMark и пиши сюда оценки.\n\nТут алгоритм работает по вот такой схеме:\nрезультат = (балл по СОР/СОЧ * 100) / макс. балл по СОР/СОЧ\nБаллы по СОР суммируются в один целый. Так же этот алгоритм предоставлен в EduMark.\n\nВАЖНО! Тут по всем четвертям прописаны по 3 СОРа и по 1 СОЧу. Если у Вас только 1 СОР и 1 СОЧ, то пишите в поле 'СОР№2' и 'СОР№3' цифру 0, дальше пишите СОЧ. Если у Вас 2 СОЧа, то суммируйте баллы по двум СОЧам в 1 целый, и пишите в поле 'СОЧ'! Иначе программа выведет оценку неправильно!\n\n\n"
if msor1_1s == 'help':
	print(colored( "\n" + help_msg + "\n", 'yellow', attrs=['bold'] ))
# иначе продолжаем работать
else: 
	msor2_1s = int(input(colored( "Макс. балл СОР№2: ", 'white', attrs=['bold'] )))
	msor3_1s = int(input(colored( "Макс. балл СОР№3: ", 'white', attrs=['bold'] )))
	msoch_1s = int(input(colored( "Макс. балл СОЧ: ", 'white', attrs=['bold'] )))
	# баллы которые ты набрал
	sor1_1s = int(input(colored( "СОР№1: ", 'white', attrs=['bold', 'dark'] )))
	sor2_1s = int(input(colored( "СОР№2: ", 'white', attrs=['bold', 'dark'] )))
	sor3_1s = int(input(colored( "СОР№3: ", 'white', attrs=['bold', 'dark'] )))
	soch_1s = int(input(colored( "СОЧ: ", 'white', attrs=['bold', 'dark'] )))

	# 2-четверть
	print("\n") # для отступа
	print(colored( "2-четверть: ", 'cyan', attrs=['bold'] ))
	# макс. баллы по СОР/СОЧ
	msor1_2s = int(input(colored( "Макс. балл СОР№1: ", 'white', attrs=['bold'] )))
	msor2_2s = int(input(colored( "Макс. балл СОР№2: ", 'white', attrs=['bold'] )))
	msor3_2s = int(input(colored( "Макс. балл СОР№3: ", 'white', attrs=['bold'] )))
	msoch_2s = int(input(colored( "Макс. балл СОЧ: ", 'white', attrs=['bold'] )))
	# баллы которые ты набрал
	sor1_2s = int(input(colored( "СОР№1: ", 'white', attrs=['bold', 'dark'] )))
	sor2_2s = int(input(colored( "СОР№2: ", 'white', attrs=['bold', 'dark'] )))
	sor3_2s = int(input(colored( "СОР№3: ", 'white', attrs=['bold', 'dark'] )))
	soch_2s = int(input(colored( "СОЧ: ", 'white', attrs=['bold', 'dark'] )))

	# 3-четверть
	print("\n") # для отступа
	print(colored( "3-четверть: ", 'cyan', attrs=['bold'] ))
	# макс. баллы по СОР/СОЧ
	msor1_3s = int(input(colored( "Макс. балл СОР№1: ", 'white', attrs=['bold'] )))
	msor2_3s = int(input(colored( "Макс. балл СОР№2: ", 'white', attrs=['bold'] )))
	msor3_3s = int(input(colored( "Макс. балл СОР№3: ", 'white', attrs=['bold'] )))
	msoch_3s = int(input(colored( "Макс. балл СОЧ: ", 'white', attrs=['bold'] )))
	# баллы которые ты набрал
	sor1_3s = int(input(colored( "СОР№1: ", 'white', attrs=['bold', 'dark'] )))
	sor2_3s = int(input(colored( "СОР№2: ", 'white', attrs=['bold', 'dark'] )))
	sor3_3s = int(input(colored( "СОР№3: ", 'white', attrs=['bold', 'dark'] )))
	soch_3s = int(input(colored( "СОЧ: ", 'white', attrs=['bold', 'dark'] )))

	# 4-четверть
	print("\n") # для отступа
	print(colored( "4-четверть: ", 'cyan', attrs=['bold'] ))
	# макс.баллы по СОР/СОЧ
	msor1_4s = int(input(colored( "Макс. балл СОР№1: ", 'white', attrs=['bold'] )))
	msor2_4s = int(input(colored( "Макс. балл СОР№2: ", 'white', attrs=['bold'] )))
	msor3_4s = int(input(colored( "Макс. балл СОР№3: ", 'white', attrs=['bold'] )))
	msoch_4s = int(input(colored( "Макс. балл СОЧ: ", 'white', attrs=['bold'] )))
	# баллы которые ты набрал
	sor1_4s = int(input(colored( "СОР№1: ", 'white', attrs=['bold', 'dark'] )))
	sor2_4s = int(input(colored( "СОР№2: ", 'white', attrs=['bold', 'dark'] )))
	sor3_4s = int(input(colored( "СОР№3: ", 'white', attrs=['bold', 'dark'] )))
	soch_4s = int(input(colored( "СОЧ: ", 'white', attrs=['bold', 'dark'] )))



	#====================================================================================================

	# вычисление

	#====================================================================================================
	# годовая
	res = ((sor1_1s + sor2_1s + sor3_1s + soch_1s + sor1_2s + sor2_2s + sor3_2s + soch_2s + sor1_3s + sor2_3s + sor3_3s + soch_3s + sor1_4s + sor2_4s + sor3_4s + soch_4s) * 100) / (int(msor1_1s) + msor2_1s + msor3_1s + msoch_1s + msor1_2s + msor2_2s + msor3_2s + msoch_2s + msor1_3s + msor2_3s + msor3_3s + msoch_3s + msor1_4s + msor2_4s + msor3_4s + msoch_4s)



	#====================================================================================================

	# выходные данные

	#====================================================================================================
	print("\n\n") # для отступа

	# годовая
	if res >= 85 and res <=100:
		print(colored( "В итоговой Вы получили " + str(int(res)) + " процентов!", 'green', attrs=['bold'] ))
		print(colored( "Оценка: 5! Поздравляю!\n\n\n", 'green', attrs=['bold'] ))
	elif res >= 65 and res <=84:
		print(colored( "В итоговой Вы получили " + str(int(res)) + " процентов!", 'green', attrs=['dark'] ))
		print(colored( "Оценка: 4! Поздравляю!\n\n\n", 'green', attrs=['dark'] ))
	elif res >= 40 and res <= 64:
		print(colored( "В итоговой Вы получили " + str(int(res)) + " процентов!", 'yellow', attrs=['bold'] ))
		print(colored( "Оценка: 3! Поздравляю!\n\n\n", 'yellow', attrs=['bold'] ))
	elif res >= 0 and res <=39:
		print(colored( "В итоговой Вы получили " + str(int(res)) + " процентов!", 'red', attrs=['bold'] ))
		print(colored( "Оценка: 2! Поздравляю!\n\n\n", 'red', attrs=['bold'] ))
	else:
		print(colored( "Данные были введены неправильно! \n\n\n", 'red', attrs=['bold'] ))
