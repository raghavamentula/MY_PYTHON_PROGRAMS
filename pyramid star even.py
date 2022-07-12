num = int(input('The number of lines in pyramid'))
for i in range(1,num+1):
    print(str(' '*(num - i))+str(('*' *i) + ('*' * i)))