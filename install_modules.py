#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Erasyl_Seralyuly

Version: no-version, гениально же ведь

Это чтобы установить необходимые модули( termcolor, colorama ) для m-discriminant.py и discriminant.py
"""
import os # модуль для управления с команадами в терминале

# прописываем команду в терминале для установки модуля termcolor для каждой из версий python
# установка модуля termcolor
os.system( 'pip install termcolor' ) # установка модуля для Python с версие 2.x
os.system( 'pip3 install termcolor' ) # установка модуля для Python с версией 3.x
# установка модуля colorama
os.system( 'pip install colorama' ) # установка модуля для Python с версией 2.x
os.system( 'pip3 install colorama' ) # установка модуля для Python с версией 3.x