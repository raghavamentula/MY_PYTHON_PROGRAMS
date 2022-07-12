import pywhatkit as kit 
print("hi welcome to send messages th is used for indian numbers")
x = input("the message u want to send:\n")
n = input("number:\n")
th = int(input("in ___ hour"))
tm = int(input("in ___ min"))
ts = int(input("in ___ sec"))
kit.sendwhatmsg("91+"+str(n),x,th,tm,ts)


