while True:
    z = int(input('write a number'))
    b = 0
    x = 0
    for a in range(1,z+1):
        b = 0
        for i in range(1,a+1):
            if a % i == 0:
                if i == 1:
                    y =  a
                elif i == a:
                    x = a
                elif i != 1 and i != a:
                    b = a
        if i == 1:
            continue
        elif x * y * b == 0:
            print(i)
        else:
            continue
