def func(n):
    i=0
    b=[]
    while i<len(n):
        if func[i] not in b:
            b.append(func[i])
        i=i+1
        print(b)
func[1,2,3,3,3,4,5]

