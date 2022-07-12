import random
op = open("D:\Rahgava Python\Games\hack.txt")
x = str(op.read())
while True:
	y = random.randint(0,int('9'*len(str(x))))
	x = int(x)
	if x == y:
		break
print('the number was',x,'the number we got is',y)
