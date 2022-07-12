from mimetypes import guess_all_extensions
import random
My_marbles = 10
User_marbles = 10
while True:
    tell_guess = input('You want me to tell or guess').lower()
    if tell_guess == 'tell':
        break
    elif tell_guess == 'guess':
        break
    else:
        print('Try again nothing found')
        continue
while True:
    if tell_guess == 'guess':
        print('\t')
        My_bet = random.randint(1,10) #the bet comp keeps
        print('My bet is',My_bet)
        My_gues = random.randint(1,2) #even or odd
        User_num = int(input('Write the number of marbles u are keeping')) #the marbles he keeps
        if My_gues == 1:
            My_guess = 'odd' 
        elif My_gues == 2:
            My_guess = 'even'
        print('I guess it is',My_guess)
        odorev = User_num % 2
        if  odorev == 0 and My_guess == 'even':
            My_marbles = My_marbles + My_bet
            User_marbles = User_marbles - My_bet
            print('My marbles are',My_marbles)
            print('your marbles are',User_marbles)
            if User_marbles <= 0:
                print('My marbles are',My_marbles,'and ur marbles are',User_marbles,'So I win')
                break
        elif odorev != 0 and My_guess == 'odd':
            My_marbles = My_marbles + My_bet
            User_marbles = User_marbles - My_bet
            print('My marbles are',My_marbles)
            print('your marbles are',User_marbles)
            if User_marbles <= 0:
                print('My marbles are',My_marbles,'and ur marbles are',User_marbles,'So I win')
                break
        else:
            print('oo.... my guess is wrong')
            My_marbles = My_marbles - My_bet
            User_marbles = User_marbles + My_bet
            print('My marbles are',My_marbles)
            print('your marbles are',User_marbles)
            if My_marbles <= 0:
                print('My marbles are',My_marbles,'and ur marbles are',User_marbles,'So U win')
                break
    elif tell_guess == 'tell':
        User_bet = int(input('the number you keep bet'))
        User_guess = input('What is ur guess even or odd')
        My_num = random.randint(1,10)
        evorod = My_num % 2
        if evorod == 0 and User_guess == 'even':
            My_marbles = My_marbles - User_bet
            User_marbles = User_marbles + User_bet
            print('My marbles are',My_marbles)
            print('your marbles are',User_marbles)
            if My_marbles <= 0:
                print('My marbles are',My_marbles,'and ur marbles are',User_marbles,'So U win')
                break
        elif evorod != 0 and User_guess == 'odd':
            My_marbles = My_marbles - User_bet
            User_marbles = User_marbles + User_bet
            print('My marbles are',My_marbles)
            print('your marbles are',User_marbles)
            if My_marbles <= 0:
                print('My marbles are',My_marbles,'and ur marbles are',User_marbles,'So U win')
                break
        else:
            My_marbles = My_marbles + User_bet
            User_marbles = User_marbles - User_bet
            print('My marbles are',My_marbles)
            print('your marbles are',User_marbles)
            if User_marbles <= 0:
                print('My marbles are',My_marbles,'and ur marbles are',User_marbles,'So I win')
                break 
print('game is done Thank You')