print('hi what is your name: \n')
name =input()
print('ok',name,'let\'s start the program')
while True:
       first = int(input('type what number table do you want:\n'))
       hio = int(input(' till when it should be multiplie by'+str(first)))
       for i in range(1,hio+1):
             sol = first * i
             ex = sol + first
             print( first ,'x',i,'=',sol)
       ver = input('do you want to still play yes or no'.lower())
       if ver == 'yes':
              continue
       elif ver =='no':
              print('ok bye')
              break

rating = input('what is your rating *')
x = len(rating)
print('Thank you for Rating',x,'stars')

       

