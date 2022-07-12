hel1 = 1000
hel2 = 1000
py1 = 0
py2 = 0
player1 = input('what is player 1 name')
player2 = input('what is player 2 name')
def1 = 0
def2 = 0
while True:
    att1 = 200
    att2 = 200
    if py1 <= 7:
        py1 += 1
    for i in range(1,py1+1):
        print('the def is for ',player1,' is ',def1)
        print('This is ',player1,' helth',hel1,'\n')
        print('This is ',player2,' helth',hel2,'\n')
        if hel2 <= 0:
            break
        elif hel1 <= 0:
            break
        print(player1,' This is the number of chances',i,'\n')
        player1_chance = input(str(player1)+' chance ATT, DEF OR INC').lower()
        if player1_chance in 'att':
            if def2 != 0:
                def2 = def2 - 1
            elif def2 == 0:
                hel2 = hel2 - att1
            print('\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n')
        elif player1_chance in 'def':
            def1 = def1 + 1
            print('\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n')
        elif player1_chance in 'inc':
             if py1 <= 7:
                py1 = py1 + 1
                print('\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n')
    if hel1 <= 0:
        print(player2,'is the winner')
        break
    elif hel2 <= 0:
        print(player1,'is the winner')
        break
        
    if py2 <= 7:
        py2 += 1
        pyy2 = py2
    for i in range(1,py2+1):
        print('the def is for ',player2,' is',def2)
        print('This is ',player2,' health',hel2,'\n')
        print('py This is ',player1,' health',hel1,'\n')
        if hel1 <= 0:
            break
        elif hel2 <= 0:
            break
        print(player2,' This is the number of chances',i,'\n')
        player2_chance = input(str(player2)+' chance ATT, DEF OR INC').lower()
        if player2_chance in 'att':
            if def1 != 0:
                def1 = def1 - 1
            elif def1 == 0:
                hel1 = hel1 - att2
            print('This is ',player1,' helth',hel1,'\n')
            print('\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n')
        elif player2_chance in 'def':
            def2 = def2 + 1
            print('\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n')
        elif player2_chance in 'inc':
            py2 == pyy2
            print('\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n')
            if py2 <= 7:
                py2 = py2 + 1
    if hel1 <= 0:
        print(player2,'is the winner')
        break
    elif hel2 <= 0:
        print(player1,'is the winner')
        break
        