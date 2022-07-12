player1 = input('enter first players name(O):\n')
player2 = input('enter second players name(X):\n')
list1 = ['l1','t','r1']
list2 = ['l2','m','r2']
list3 = ['l3','b','r3']
true = False
true1 = False
l1 =list1[0]
l2 =list2[0]
l3 =list3[0]
t =list1[1]
m = list2[1]
b = list3[1]
r1 = list1[2]
r2 = list2[2]
r3 =list3[2] 
print('Take this and type,\n')
print(list1)
print(list2)
print(list3,'\n')
w = 0 
j = 0
def main1():
    global true
    if list1[0] == 'O' and list1[1] == 'O' and list1[2] == 'O':
        print('o won the game')
        true = True
    elif list2[0] == 'O' and list2[1] == 'O' and list2[2] == 'O':
        print('o won the game')
        true = True
    elif list3[0] == 'O' and list3[1] == 'O' and list3[2] == 'O':
        print('o won the game')
        true = True
    elif list1[0] == 'O' and list2[0] == 'O' and list3[0] == 'O':
        print('o won the game')
        true = True
    elif list1[1] == 'O' and list2[1] == 'O' and list3[1] == 'O':
        print('o won the game')
        true = True
    elif list1[2] == 'O' and list2[2] == 'O' and list3[2] == 'O':
        print('o won the game')
        true = True
    elif list1[0] == 'O' and list2[1] == 'O' and list3[2] == 'O':
        print('o won the game')
        true = True
    elif list3[0] == 'O' and list2[1] == 'O' and list1[2] == 'O':
        print('o won the game')
        true = True

def main2():
    global true1
    if list1[0] == 'X' and list1[1] == 'X' and list1[2] == 'X':
        print('X won the game')
        true1 = True
    elif list2[0] == 'X' and list2[1] == 'X' and list2[2] == 'X':
        print('X won the game')
        true1 = True
    elif list3[0] == 'X' and list3[1] == 'X' and list3[2] == 'X':
        print('X won the game')
        true1 = True
    elif list1[0] == 'X' and list2[0] == 'X' and list3[0] == 'X':
        print('X won the game')
        true1 = True
    elif list1[1] == 'X' and list2[1] == 'X' and list3[1] == 'X':
        print('X won the game')
        true1 = True
    elif list1[2] == 'X' and list2[2] == 'X' and list3[2] == 'X':
        print('X won the game')
        true1 = True
    elif list1[0] == 'X' and list2[1] == 'O' and list3[2] == 'X':
        print('X won the game')
        true1 = True
    elif list3[0] == 'X' and list2[1] == 'X' and list1[2] == 'X':
        print('X won the game')
        true1 = True
        
while True:
    ch1 = input('\n')
    if ch1 == 'l1' and list1[0] != 'X':
        list1[0] = 'O'
        print(list1)
        print(list2)
        print(list3,'\n')
        main1()
        if true == True:
            break
    elif ch1 == 't' and list3[2] != 'X':
        list1[1] = 'O'
        print(list1)
        print(list2)
        print(list3,'\n')
        main1()
        if true == True:
            break
    elif ch1 == 'r1' and list1[2] != 'X':
        list1[2] = 'O'
        print(list1)
        print(list2)
        print(list3,'\n')
        main1()
        if true == True:
            break
    elif ch1 == 'l2' and list2[0] != 'X':
        list2[0] = 'O'
        print(list1)
        print(list2)
        print(list3,'\n')
        main1()
        if true == True:
            break
    elif ch1 == 'm' and list2[1] != 'X':
        list2[1] = 'O'
        print(list1)
        print(list2)
        print(list3,'\n')
        main1()
        if true == True:
            break
    elif ch1 == 'r2' and list2[2] != 'X':
        list2[2] = 'O'
        print(list1)
        print(list2)
        print(list3,'\n')
        main1()
        if true == True:
            break
    elif ch1 == 'l3' and list3[0] != 'X':
        list3[0] = 'O'
        print(list1)
        print(list2)
        print(list3,'\n')
        main1()
        if true == True:
            break
    
    elif ch1 == 'b' and list3[1] != 'X':
        list3[1] = 'O'
        print(list1)
        print(list2)
        print(list3,'\n')
        main1()
        if true == True:
            break
    elif ch1 == 'r3' and list3[2] != 'X':
        list3[2] = 'O'
        print(list1)
        print(list2)
        print(list3,'\n')
        main1()
        if true == True:
            break
    elif list1[0] != 'l1' and list2[0] != 'l2' and 'l3' != list3[0] and 'm' != list3[1] and list3[1] !='b' and list1[2] != 'r1' and  list2[2] != 'r2' and list3[2]!= 'r3':
        print('Draw')
        break
    
    else:
        print('ERROR')
        break
    ch2 = input('\n')
    if ch2 == 'l1' and list1[0] != 'O':
        list1[0] = 'X'
        print(list1)
        print(list2)
        print(list3,'\n')
        main2()
        if true1 == 1:
            break
    elif ch2 == 't' and list1[1] != 'O':
        list1[1] = 'X'
        print(list1)
        print(list2)
        print(list3,'\n')
        main2()
        if true1 == 1:
            break
    elif ch2 == 'r1' and list1[2] != 'O':
        list1[2] = 'X'
        print(list1)
        print(list2)
        print(list3,'\n')
        main2()
        if true1 == 1:
            break
    elif ch2 == 'l2' and list2[0] != 'O':
        list2[0] = 'X'
        print(list1)
        print(list2)
        print(list3,'\n')
        main2()
        if true1 == 1:
            break
    elif ch2 == 'm' and list2[1] != 'O':
        list2[1] = 'X'
        print(list1)
        print(list2)
        print(list3,'\n')
        main2()
        if true1 == 1:
            break
    elif ch2 == 'r2' and list2[2] != 'O':
        list2[2] = 'X'
        print(list1)
        print(list2)
        print(list3,'\n')
        main2()
        if true1 == 1:
            break
    elif ch2 == 'l3' and list3[0] != 'O':
        list3[0] = 'X'
        print(list1)
        print(list2)
        print(list3,'\n')
        main2()
        if true1 == 1:
            break
    elif ch2 == 'b' and list3[1] != 'O':
        list3[1] = 'X'
        print(list1)
        print(list2)
        print(list3,'\n')
        main2()
        if true1 == 1:
            break
    elif ch2 == 'r3' and list3[2] != 'O':
        list3[2] = 'X'
        print(list1)
        print(list2)
        print(list3,'\n')
        main2()
        if true1 == 1:
            break
    else:
        print('ERROR')
        break
