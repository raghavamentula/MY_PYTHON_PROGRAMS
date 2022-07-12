import random
print(' welcome to rock paper sicssor game')
name = input('what is your name: \n   ')
print('ok ',name,'let us start the game')
while True:
       guess =input('what do u want to choose.Rock paper or sicssor:\n').lower()
       if guess == 'rock':
              print('so ur choise is rock')
              break
       elif guess == 'paper':
              print('so ur choise is paper ')
              break
       elif guess == 'sicssor':
              print('so ur choise is sicssor ')
              break
       else:
              print('Their is nothing named',str(guess))
win =' YaY!! you won the game'
lost =' Opps you lost the game'
draw ='the game is draw'
random = random.randint(1,3)
if guess == 'rock' and random == 2:
       print(lost)
elif  guess == 'paper' and random == 1:
       print(win)
elif guess == 'paper' and random == 3:
       print(lost)
elif guess == 'sicssor' and random == 2:
       print(win)
elif guess == 'rock' and random == 3:
       print(win)
elif guess == 'sicssor' and random == 1:
       print(lost)
elif guess == 'rock' and random == 1:
       print(draw)
elif guess == 'sicssor' and random == 3:
       print(draw)
elif guess == 'paper' and random == 2:
       print(draw)
else:
       print('I don\'t know')
if random == 1:
      print('the computer chosen  was Rock')

elif random == 2:
       print('the computer chosen  was paper')
       
elif random == 3:
       print('the computer chosen  was sicssor')

