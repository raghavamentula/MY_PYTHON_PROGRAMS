import time as t , random as r
print('welcome to the game')
hell1 = 1000
att1  = 100
hell2 = 1000
att2  = 100
player1 = input('player 1 name plz')
player2 = input('player 2 name plz')
print(player1,'turn')
a = t.time()
while True:
       ran1 = r.randint(1000,9999)
       print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'+str(ran1)+'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
       ans1 = int(input('Write Answer'))
       if ran1 == ans1:
              hell2 = hell2 - att1
              print(hell2)
              if hell2 == 0:
                     break
       elif ans1 == ran1:
              print('Wrong answer')
b = t.time()
c = b - a
c = int(c)
print(c)
print(player2,'turn')
z = t.time()
while True:
       ran2 = r.randint(1000,9999)
       print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'+str(ran2)+'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
       ans2 = int(input('Write Answer'))
       if ran2 == ans2:
              hell1 = hell1 - att2
              print(hell1)
              if hell1 == 0:
                     break
       elif ans2 == ran2:
              print('Wrong answer')
y = t.time()
x = y - z
x = int(x)
print(x)
if x > c:
       print(player1,'won the game')
elif x < c:
       print(player2,'won the game')
elif x == c:
       print('This game is a Draw')
else:
       print('...??????????')
              
