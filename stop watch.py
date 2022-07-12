import time
while True:
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
       ver = input('do you want to keep a sto watch agin.???')
       if ver == 'yes':
              continue
       elif ver == 'no':
              break
       else:
              print('sorry I don\'t  know I am runnin it again')
              
