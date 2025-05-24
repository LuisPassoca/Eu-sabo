import time
import os
import random

clear = lambda: os.system('cls')
roleta = 0
roletada = random.randint(6, 30)
roletaspd = 0.3
clear()
print('Número de roletadas', roletada-1)
time.sleep(2)
clear()

while roletada > 0:
    if roleta == 0 or 2 and roletada >= 1:
        print('   V')
        print('   1   ')
        roleta = 1
        roletada -= 1
        print('6     2')
        print('5     3')
        print('   4   ')
        time.sleep(roletaspd)
        if roletada == 0:
            time.sleep(1)
        clear()
    if roleta == 1 and roletada >= 1:
        print('   V')
        print('   6   ')
        roleta = 6
        roletada -= 1
        print('5     1')
        print('4     2')
        print('   3   ')
        time.sleep(roletaspd)
        if roletada == 0:
            time.sleep(1)
        clear()
    if roleta == 6 and roletada >= 1:
        print('   V')
        print('   5   ')
        roleta = 5
        roletada -= 1
        print('4     6')
        print('3     1')
        print('   2   ')
        time.sleep(roletaspd)
        if roletada == 0:
            time.sleep(1)
        clear()
    if roleta == 5 and roletada >= 1:
        print('   V')
        print('   4   ')
        roleta = 4
        roletada -= 1
        print('3     5')
        print('2     6')
        print('   1   ')
        time.sleep(roletaspd)
        if roletada == 0:
            time.sleep(1)
        clear()
    if roleta == 4 and roletada >= 1:
        print('   V')
        print('   3   ')
        roleta = 3
        roletada -= 1
        print('2     6')
        print('1     5')
        print('   6   ')
        time.sleep(roletaspd)
        if roletada == 0:
            time.sleep(1)
        clear()
    if roleta == 3 and roletada >= 1:
        print('   V')
        print('   2   ')
        roleta = 2
        roletada -= 1
        print('1     3')
        print('6     4')
        print('   5   ')
        time.sleep(roletaspd)
        if roletada == 0:
            time.sleep(1)
        clear()



print('Parabéns! Tirou', roleta)
