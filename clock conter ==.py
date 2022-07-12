hou = int(input('Hi wlecome hour plz:\n'))
minu = int(input('minutes plz:\n'))
sec = int(input('seconds plz:\n'))
while True:
       if sec >= 60:
              sec = sec - 60
              minu = minu + 1
       if minu >= 60:
              minu  = minu - 60
              hou = hou + 1
       if minu < 60 and sec < 60:
              break
hou = str(hou)
minu = str(minu)
sec = str(sec)
print('hours = '+ hou +' minutes = '+ minu +' seconds = '+ sec )
       

       
