print('welcome to rigito game')
while True:
       username = input('Username : \n'.lower())
       password = input('Password : \n'.lower())
       if username == 'raghava' and password == 'ragito':
              print('you are valid')
              break
       else:
              if username != 'raghava' and password != 'rigito':
                     print('Username and Password are invalid')
              elif username != 'raghava':
                     print('Username is in valid')
              elif password != 'rigito':
                     print('Password is invalid')
              else:
                     print('Username and Password in valid')
while True:
       game = input('what game do u want to play. Addition game1 , Addition game2 , AttDefCon , EveaOdd , file , guess the num , logogame , rps(Rockpaperseciors) , table , timer , stopwatch , clock , hand cricket , quiz creater \n'.lower())

       if game == 'addition game1':
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
              
       elif game == 'attdefcon':
              helone = 1000
              heltwo = 1000
              attone = 100
              atttwo = 100
              conone = 100
              contwo = 100
              print('hi welcome to attdefcon game this is a two player game')
              nameone=input('what is player1\'s name')
              nametwo=input('what is player2\'s name')
              print('ok ' + nameone + ' and ' + nametwo + ' let\'s start the game')
              print('you both have 1000 helath and 100 attake for each of you')
              print('Att = 100 damage Def = 90 add life Con for double attack But,only for one time')
              while True:
                     whatone =input('now it is '+nameone+'turn').lower()
                     if whatone == 'att':
                            heltwo = heltwo-attone
                            print(str(heltwo)+' hel for '+str(nametwo))
                            attone = 100
                     elif whatone =='def':
                            helone = helone + 90
                            print('now health of ' + nameone  + ' is ' +str(helone))
                     elif whatone == 'con':
                            attone = attone + attone
                            print('now your attack power is dobled')
                     else:
                            print('I don\'t know '+whatone+' can you tell again')
                     whattwo =input('now it is '+nametwo+' turn').lower()
                     if whattwo == 'att':
                            helone = helone - atttwo
                            print(str(helone)+'hel for'+str(nameone))
                            atttwo = 100
                     elif whattwo =='def':
                            heltwo = heltwo + 90
                            print('now health of ' + nametwo + ' is ' +str(heltwo))
                     elif whattwo == 'con':
                            atttwo = atttwo + atttwo
                            print('now your attack power is dobled')
                     if helone <= 0:
                            print(nametwo,' won')
                            break
                     elif heltwo <= 0:
                            print(nameone,' won')
                            break
               
       elif game == 'evenodd':
              num = int(input('write the number to ckeak it is a even or an odd number:\n'))
              if (num  %  2) == 0:
                     print(num,'is an even')
              else:
                     print(num,'is an odd')
              
       elif game == 'file':
              tell =input('what do u want to do write a path or document name but document name should be in same folder\n doc or path:')
              if tell == 'doc':
                     ty =input('doc name')
                     x = ty  +'.txt'
                     y = open(x)
                     print(y.read())
              
              elif tell == 'path':
                     ly =input("write the path without string")
                     x = open(ly)
                     print(x.read())
       
              else:
                     print('this is nothing named',tell)
              
       elif game == 'guess the num':
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
              
       elif game == 'logogame':
              import random
              name = input('hi welcome to logo game ,what is your name:\n')
              print('ok' , name ,'we have  question based on social media,and you have to answer ')
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
              while True:
                     ans = input('write the answer\n').lower()
                     win = 'you are correct'
                     if randa == 1 and ans == 'facebook':
                            print(win)
                            break
                     elif randa == 2 and ans == 'instagram':
                            print(win)
                            break
                     elif randa == 3 and ans == 'google':
                            print( win)
                            break
                     elif randa == 4 and ans == 'snapchat':
                            print(win)
                            break
                     elif randa == 5 and ans == 'youtube':
                            print(win)
                            break
                     elif randa == 6 and ans == 'twitter':
                            print (win)
                            break
                     elif randa == 7 and ans == 'pubg':
                            print(win)
                            break
                     else:
                            print('your ans is wrong')      
              
       elif game =='rps':
              import random
              print(' welcome to rock paper sicssor game')
              name = input('what is your name: \n   ')
              print('ok ',name,'let us start the game')
              while True:
                     guess =input('what do u want to choose.Rock paper or sicssor').lower()
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
                     print('the computer chosen Rock')
              elif random == 2:
                     print('the computer chosen paper')
              elif random == 3:
                     print('the computer chosen sicssor')
              
       elif game == 'table':
              print('hi what is your name: \n')
              name =input()
              print('ok',name,'let\'s start the program')
              first = int(input('type what number table do you want:\n'))
              hio = int(input(' till when it should be multiplie by'+str(first)))
              for i in range(1,hio + 1):
                     sol = first * i
                     ex = sol + first
                     print( first ,'x',i,'=',sol)
       elif game == 'addition game2':
              print('welcome to 2 digit number Game for kids')
              name = input('What is yourm name:    ')
              while True:
                     import random
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
                     verify = input('do want to play addition again yes or no')
                     if verify == 'yes':
                            continue
                     elif verify == 'no':
                            break
       elif game == 'timer':
              import time,playsound
              z = time.ctime()
              sec  = int(input('sec plz\n'))  
              minu = int(input('min plz \n'))
              x = input('click enter to start')
              while True:
                     if minu > 0:
                            sec = sec + 60
                            minu = minu - 1
                     if minu == 0:
                            break
              time.sleep(sec)
              playsound.playsound("H:/Rahgava Python/raghava.wma")
       elif game == 'stopwatch':
              import time
              mi = 0    
              ho = 0
              x = input('enter')
              y = time.time()
              z = input('end')
              a = time.time()
              b = a - y
              b = int(b)
              while True:
                     if b  >= 60:
                            mi = mi +1
                            b = b - 60
                            if b >= 60:
                                   continue
                     if mi >= 60:
                            ho = ho + 1
                            mi = mi - 60
                            if mi >= 60:
                                   continue
                     if b < 60 and mi < 60:
                            break
              print(str(ho) + ' hours ' +str(mi) + ' minutes ' + str(b) + ' seconds')
       elif game == 'clock':
              import time,playsound
              print('hi welcome to the clock ')
              while True:
                     f = input('timer or stopwatch'.lower()) 
                     if f == 'timer':
                            z = time.ctime()
                            sec  = int(input('sec plz\n'))
                            minu = int(input('min plz \n'))
                            x = input('click enter to start')
                            while True:
                                   if minu > 0:
                                          sec = sec + 60
                                          minu = minu - 1
                                   if minu == 0:
                                          break
                            time.sleep(sec)
                            playsound.playsound("H:/Rahgava Python/raghava.wma")
                     elif f == 'stopwatch':
                            mi = 0
                            ho = 0
                            x = input('enter')
                            y = time.time()
                            z = input('end')
                            a = time.time()
                            b = a - y
                            b = int(b)
                            while True:
                                   if b  >= 60:
                                          mi = mi +1
                                          b = b - 60
                                          if b >= 60:
                                                 continue
                                   if mi >= 60:
                                          ho = ho + 1
                                          mi = mi - 60
                                          if mi >= 60:
                                                 continue
                                   if b < 60 and mi < 60:
                                          break
                            print(str(ho) + ' hours ' +str(mi) + ' minutes ' + str(b) + ' seconds')
                     elif f == 'alarm':
                            import time as t , playsound as p ,re
                            l = t.ctime()
                            l  = str(l)
                            x = re.compile('\d\d:\d\d:\d\d')
                            y = x.findall(l)
                            print('Now Time is:', y)
                            hou = str(input('hours plz ex = 01 or 22'))
                            minu =  str(input('minutes plz ex = 01 or 22'))
                            sec =  str(input('seconds plz ex = 01 or 22'))
                            tim =  hou+':' + minu + ':' + sec
                            tim = [tim]
                            print('alarm set for',tim)
                            while True:
                                   l = t.ctime()
                                   l = str(l)
                                   x = re.compile('\d\d:\d\d:\d\d')
                                   y = x.findall(l)                     
                                   if tim == y:
                                          break
                            print('alarm set for',tim)
                            p.playsound("H:/Rahgava Python/raghava.wma")
                            vr = input('do do want to play clock agin yes or no'.lower())
                            if vr == 'yes':
                                   continue
                            elif vr == 'no':
                                   break
       elif game == 'hand cricket':
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
       elif game == 'quiz creater':
              c = 'correct answer'
              w = 'wrong answer'
              print('welcome to quiz creater you can costomize 5 questions')
              q1 = input('write the title for 1st question:\t'.lower())
              a1 = input('Option a:\t'.lower())
              b1 = input('option b:\t'.lower())
              c1 = input('option c:\t'.lower())
              d1 = input('option d:\t'.lower())
              ans1 = input('What is the answer a b c d:\t '.lower())
              print('Question display')
              print(q1)
              print('a.)',a1,'\tb.)',b1)
              print('c.)',c1,'\td.)',d1)

              q2 = input('write the title for 2st question:\t'.lower())
              a2 = input('Option a:\t'.lower())
              b2 = input('option b:\t'.lower())
              c2 = input('option c:\t'.lower())
              d2 = input('option d:\t'.lower())
              ans2 = input('What is the answer a b c d :\t'.lower())
              print('Question display')
              print(q2)
              print('a.)',a2,'\tb.)',b2)
              print('c.)',c2,'\td.)',d2)
             
              q3 = input('write the title for 3st question:\t'.lower())
              a3 = input('Option a:\t'.lower())
              b3 = input('option b:\t'.lower())
              c3 = input('option c:\t'.lower())
              d3 = input('option d:\t'.lower())
              ans3 = input('What is the answer a b c d:\t '.lower())
              print('Question display')
              print(q3)
              print('a.)',a3,'\tb.)',b3)
              print('c.)',c3,'\td.)',d3)
             
              q4 = input('write the title for 4st question:\t'.lower())
              a4 = input('Option a:\t'.lower())
              b4 = input('option b:\t'.lower())
              c4 = input('option c:\t'.lower())
              d4 = input('option d:\t'.lower())
              ans4 = input('What is the answer a b c d :\t'.lower())
              print('Question display')
              print(q4)
              print('a.)',a4,'\tb.)',b4)
              print('c.)',c4,'\td.)',d4)
             
              q5 = input('write the title for 3st question:\t'.lower())
              a5 = input('Option a:\t'.lower())
              b5 = input('option b:\t'.lower())
              c5 = input('option c:\t'.lower())
              d5 = input('option d'.lower())
              ans5 = input('What is the answer a b c d :\t'.lower())
              print('Question display')
              print(q5)
              print('a.)',a5,'\tb.)',b5)
              print('c.)',c5,'\td.)',d5)
              print('now the quiz start\'s')
              print(q1)
              print('a.)',a1,'\tb.)',b1)
              print('c.)',c1,'\td.)',d1)
              write1 = input('what is answer:\t')
              if write1 == ans1:
                     print(c)
              else:
                     print(w)
              print(q2)
              print('a.)',a2,'\tb.)',b2)
              print('c.)',c2,'\td.)',d2)
              write2 = input('what is answer:\t')
              if write2 == ans2:
                     print(c)
              else:
                     print(w)
              print(q3)
              print('a.)',a3,'\tb.)',b3)
              print('c.)',c3,'\td.)',d3)
              write3 = input('what is answer:\t')
              if write3 == ans3:
                     print(c)
              else:
                     print(w)
              print(q4)
              print('a.)',a4,'\tb.)',b4)
              print('c.)',c4,'\td.)',d4)
              write4 = input('what is answer:\t')
              if write4 == ans4:
                     print(c)
              else:
                     print(w)
              print(q5)
              print('a.)',a5,'\tb.)',b5)
              print('c.)',c5,'\td.)',d5)
              write5 = input('what is answer:\t')
              if write5 == ans5:
                     print(c)
              else:
                     print(w)

       else:
              print('their is noting named',game)
       verify = input('do want to play rigito again yes or no')
       if verify == 'yes':
              continue
       elif verify == 'no':
              break
       
       
