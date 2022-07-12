import random
name = input('hi what is your name:\n')
print('hi nice meeting u',name,'My name is guess the number game what level do u want to play. Easy has 1 to 2 numbers, Medium has 1 to 4 number, Hard has 1 to 6 number But, u have only one chance ')
level = input().lower()
def game():
        if guess > num:
              print('too high')
        elif guess < num:
              print('too low')
        if guess != num:
              print('no the num is ',num)
        elif guess == num:
              print('you won the game!')
if level == 'hard':
       guess = int(input('enter a number\n'))
       num = random.randint(1, 6)
       game()
elif level == 'medium':
       guess = int(input('enter a number\n'))
       num = random.randint(1, 4)
       game()   
elif level == 'easy':
       guess = int(input('enter a number\n'))
       num = random.randint(1, 2)
       game()
             
       

       
       
       

       
       
