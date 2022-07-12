import keyboard
helone = 1000
heltwo = 1000
attone = 100
atttwo = 100
conone = 100
contwo = 100
defone = 90
deftwo = 90
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
              helone = helone + defone
              print('now health of ' + nameone  + ' is ' +str(helone))
              defone = 90
       elif whatone == 'con':
              i = input('100 should be added to att(attck) or def(defence)'.lower())
              if i == 'att':
                     attone = attone * 2
                     print('your attack is doubled')
              elif i == 'def':
                     defone = defone * 2
                     print('your defence is doubled')
       else:
              print('I don\'t know '+whatone)
              break
       if helone <= 0:
              print(nametwo,' won')
              break
       elif heltwo <= 0:
              print(nameone,' won')
              break
       whattwo =input('now it is '+nametwo+' turn').lower()
       if whattwo == 'att':
              helone = helone - atttwo
              print(str(helone)+'hel for'+str(nameone))
              atttwo = 100
       elif whattwo =='def':
              heltwo = heltwo + deftwo
              print('now health of ' + nametwo + ' is ' +str(heltwo))
              deftwo = 90
       elif whattwo == 'con':
              a = input('100 should be added to att(attck) or def(defence)'.lower())
              if a == 'att':
                     atttwo = atttwo * 2
                     print('your attack is doubled')
              elif a == 'def':
                     deftwo = deftwo * 2
                     print('your defence is doubled')
              else:
                     print('I don\'t know '+whattwo)
                     break 
       if helone <= 0:
              print(nametwo,' won')
              break
       elif heltwo <= 0:
              print(nameone,' won')
              break
       
 
       



              
              

       
       
