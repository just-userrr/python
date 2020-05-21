#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Это чтобы установить необходимые модули( termcolor, colorama ) для других программ, которые требуют этих модулей
"""
import os # модуль для управления с команадами в терминале

# прописываем команду в терминале для установки модуля termcolor для каждой из версий python
# установка модуля termcolor
os.system( 'pip install termcolor' ) # установка модуля для Python с версие 2.x
os.system( 'pip3 install termcolor' ) # установка модуля для Python с версией 3.x
# установка модуля colorama
os.system( 'pip install colorama' ) # установка модуля для Python с версией 2.x
os.system( 'pip3 install colorama' ) # установка модуля для Python с версией 3.x
