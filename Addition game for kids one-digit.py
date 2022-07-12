import random
print('welcome to 1 digit number Game for kids')
name = input('What is yourm name:    ')

while True:
       age = int(input('what is your Age:   '))
       if age < 11 and age > 3: 
              print('your welcome bcz your age is less eleven and greated then three')
              break
al = random.randint(0, 9)
num = random.randint(0, 9)
tot = al + num
print(al,'+',num)
ans = int(input('Write the solution:    '))
if tot == ans:
       print('your correct')
else:
       print('your ans is wrong the ans is',al + num)
       
       
       


       
