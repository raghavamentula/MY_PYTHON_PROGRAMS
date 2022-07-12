import time,playsound
print('hi welcome to the clock ')
sound = "D:/Rahgava Python/raghava.wma"
while True:
       f = input('timer or stopwatch or alarm'.lower())
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
              playsound.playsound(sound)
                     
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
              l = str(l)
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
              p.playsound(sound)
       verify = input('do u want to play again')
       if verify == 'yes':
              continue
       else:
              break
