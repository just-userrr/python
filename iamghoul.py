#
#   | ┌───┐ ┌───┐ ┌───┐        ──────
#  /| |   | |   | |   |             /
#   | |   | |   | |   |  ────      /
#   | |   | |   | |   |           /
#   | └───┘ └───┘ └───┘          /
#

import time
import math

n = 1000
for i in range(math.floor(1000/7)):
	m = n - 7
	print(str(n) + " - 7 = " + str(m))
	time.sleep(0.1)
	n -= 7
