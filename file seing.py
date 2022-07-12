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
       






