def func():
    i=1
    b=[]
    m=[]
    while i<=5:
        c=i*i
        b.append(c)
        i+=1
    print(b)
    j=25
    k=[]
    while j<=30:
        d=j*j
        k.append(d)
        j+=1
    print(k)
    m.append(b)
    m.append(k)
    print(m)
    
func()     