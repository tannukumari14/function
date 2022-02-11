def perfect():
    a=int(input("enter the number"))
    sum=0
    i=1
    while a>i:
        if a%i==0:
            sum=sum+i
            i=i+1
        if sum==a:
            print(a,"perfect number")
    else:
        print(a,"not perfect")
perfect()