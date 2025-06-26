def Odd(hari:int)->int:
    if hari%2==0:
        count=hari-1
    else:
        count=hari

    a=[]
    b=1
    while len(a)<count:
        a.append(b)
        b+=2
    return ','.join(map(str,a))


print(Odd(int(input('Enter Your Value : '))))

