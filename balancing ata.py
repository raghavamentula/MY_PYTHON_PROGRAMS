import time
import mouse
print('hi welcome to this game')
omg = (input('what to play easy ,medium ,hard ,rapid hard ,impossible').upper())
print(omg)
if omg == 'EASY':
    print('ok let\'s start the game')
    print('now balance the rubber')
    for i in range(0,110,10):
        time.sleep(1)
        print(str(i)+'%')
        if True == True:
            time.sleep(0.1)
            inp = input()

        if i == 50 and inp == '':
            break
    print('you won the game')
        