def Odd(input:int)->int:
    a=[]
    b=1
    while len(a)<input:
        if b%2!=0:
            a.append(b)
        b+=1
    return a

print(Odd(int(input('Enter the Value : '))))
