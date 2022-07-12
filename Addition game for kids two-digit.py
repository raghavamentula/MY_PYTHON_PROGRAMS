import random
print('welcome to 2 digit number Game for kids')
name = input('What is yourm name:    ')
while True:
       al = random.randint(10,99)
       num = random.randint(10,99)
       tot = al + num
       print(' ', al)
       print('+',num)
       ans = int(input('  '))
       if tot == ans:
              print('your correct')
       elif tot != ans:
              print('Wrong answer . the answer is',str(tot))
              
