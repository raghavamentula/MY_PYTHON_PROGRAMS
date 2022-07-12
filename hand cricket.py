import random
print('hi welcome to hand cricket')
while True:
       a =input('write bat or ball'.lower())
       if a == 'bat':
              y = 0
              ran = random.randint(1,6)
              for i in range(1,100000000000):
                     while True:
                            x = int(input('ok what is your '+str(i)+' number'))
                            if x <=  6:
                                   break
                            elif x > 7:
                                   print('the number should be till 6 only')
                     y = x + y
                     
                     if x == ran:
                            break
              print('your bating is over because ur outted')
              print('your score is',y)
              print('now its time for computer for bating')
              h = 0
              for i in range(1,1000000000000000):
                     randa = random.randint(1,6)
                     b = int(input('write a number betwen 1, 6number'))
                     h = randa + h
                     if randa == b:
                            break
              print('the computer score is '+str(h))
              if h > y:
                     print('you lost the game:(')
              elif h < y:
                     print('you won the game:)')
              elif h == y:
                     print('the game is draw')
                            
       elif a == 'ball':
              y = 0
              for i in range(1,100000):
                     rand = random.randint(1,3)
                     while True:
                            z = int(input('write a number betwen 1, 6number'))
                            if z >= 4:
                                   print('number should be less than 7')
                            elif z <= 3:
                                   break
                     y = rand + y
                     if rand == z:
                            break
              print('score of computer is'+str(y))
              m = 0
              ran = random.randint(1,6)
              for i in range(1,100000000000):
                     while True:
                            x = int(input('ok what is your '+str(i)+' number'))
                            if x <= 6:
                                   break
                            elif x > 7:
                                   print('the number should be till 6 only')
                     m = x + m
                     
                     if x == ran:
                            break
              print('your score is'+str(m))
              if m > y:
                     print('you won the game:)')
              elif m < y:
                     print('you lost the game:(')
              elif m == y :
                     print('drraw')
       verify = input('do you want to play again'.lower())
       if verify == 'yes':
              continue
       elif verify == 'no':
              break
       
                     
              

                            
                     
              
              
                     

                     
                     
