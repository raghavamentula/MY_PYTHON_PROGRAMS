while True:
    z = int(input())
    a = 0
    for i in range(1,z+1):
        if z % i == 0:
            if i == 1:
                y =  i
            elif i == z:
                x = i
            elif i != 1 and i != z:
                a = i
            
            print(i)
    if z == 1:
        print('none of the above\n')
    elif z == 0:
        print('none of the above\n')
    elif x * y * a == 0:
        print('yes it is a prime number\n')
    elif x * y * a != 0:
        print('no it is a prime number\n')
    

    

        
