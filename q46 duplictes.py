def func(*a):
    b=[]
    i=0
    while i<len(a):
        if a[i]  not in b:
            b.append(a[i])
        i=i+1
    print(b)
func(9,1,2,3,2,5,6)
