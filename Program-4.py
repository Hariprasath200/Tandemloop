def Count(hari:list)->dict:
    print('h',hari)
    result={i:0 for i in range(1,10)}
    for h in hari:
        for i in range(1,10):
            if h%i==0:
                result[i]+=1
    return result

a=input('Enter the Value : ')
lists=[int(x) for x in a.split(',')]
print(Count(lists))