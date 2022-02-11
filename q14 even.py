# def function(n):
#     i=0
#     while i<len(n):
#         if n[i]%2==0:
#             print(n[i],"even")
#         else:
#             print(n[i],"odd")
#         i=i+1
# function([79,4,2,7,8,54])


# def isEven(n):
#     num=int(input("enter the number"))
#     if(num%2==0):
#         print("Even Number")
#     else:
#         print("Odd Number")
# isEven("even")

# def function(a,b):
#     i=0
#     while i<len(a):
#         if a[i]%2==0 and b[i]%2==0:
#             print(a[i],b[i]," dono even hai")
#         else:
#             print(a[i],b[i],"dono odd hai")
#         i=i+1
# function([2,6,18,10,3,75],[8,9,76,54,34,2])

# def func(*n):
#     i=0
#     while i<len(n):
#         if n[i]%2==0:
#             print(n[i],"even")
#         i=i+1
# func(1,2,3,4,5,6,7,8,9)

def func(a):
    i=0
    while i<len(a):
        if a[i]%2==0:
            print(a[i],"even")
        else:
            print(a[i],"odd")
        i=i+1
func([10,2,4,56,9,0])