import time,playsound
z = time.ctime()
while True:
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
       playsound.playsound("D:/Rahgava Python/raghava.wma")
       verify = input('do want another timer yes or no..?\n')
       if verify == 'yes':
              continue
       elif verify == 'no':
              break
       else:
              print('I don\'t know '+verify+' I am repeeting again')
              continue

              





