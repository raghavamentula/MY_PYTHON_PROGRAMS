import random
name = input('hi welcome to logo game ,what is your name:\n')
print('ok' , name ,'we have  question based on social media,and you have to \
      answer ')
randa = random.randint(1,7)
if randa == 1:
       print('f')
elif randa == 2:
       print('camera')
elif randa == 3:
       print('G')
elif randa == 4:
       print('ghost')
elif randa == 5:
       print('palybutton')
elif randa == 6:
       print('bird')
elif randa == 7:
       print('man with a gun')

ans = input('write the answer\n').lower()
win = 'you are correct'
if randa == 1 and ans == 'facebook':
       print(win)
elif randa == 2 and ans == 'instagram':
       print(win)
elif randa == 3 and ans == 'google':
       print( win)
elif randa == 4 and ans == 'snapchat':
       print(win)
elif randa == 5 and ans == 'youtube':
       print(win)
elif randa == 6 and ans == 'twitter':
       print (win)
elif randa == 7 and ans == 'pubg':
       print(win)
else:
       print('your ans is wrong')
