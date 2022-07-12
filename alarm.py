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
p.playsound("D:\Rahgava Python\raghava.wma")
