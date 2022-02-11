# def sum(n):
#     print(12+13)
# sum(12+13)

# def num(n):
#     print(sum(n),"sum")
# num([1,2,3,4,5])

# def function(number1,number2):
#     num3=number1+number2
#     print(num3)
# function(56,12)

# def add_number_list(a,b):
#     i=0
#     while i<len(a):
#         print(a[i]+b[i])
#         i+=1
# add_number_list([50,60,10],[10,20,13])

# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum
# sum1 = add_numbers(20, 40)
# print(sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print(sum2)
# print(sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print(number_a)


# def add_numbers(num1,num2):
#     sum=num1+num2
#     return sum
# num1=add_numbers(20,40)
# print(num1)
# num2=add_numbers(90,345)
# a=1345
# b=98
# num3=add_numbers(a,b)
# print(num2)
# print(num3)
# number_b =add_numbers(5, 4) / add_numbers(2, 1)
# print(number_b)

# def add_numbers_print(number_x, number_y):
#     sum = number_x + number_y
#     print (sum)
# add_numbers_print(4,5)
# print(type(sum))

# def add_numbers(x,y):
#     sum = x + y
#     print("Hello from NavGurukul ;)")
#     sum = x + y
#     print(sum)
#     print("Kya main yahan tak pahunchunga?")
# sum6 = add_numbers(100, 20)

# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"
# print("Kya main print ho payungi? :-(")
# mon_menu = menu("monday")
# print(mon_menu)
# tues_menu = menu("tuesday")
# print(tues_menu)
# fri_menu = menu("friday")
# # print(fri_menu)

# def menu(day):
#     if day == "monday":
#         food = "Butter Chicken"
#     elif day == "tuesday":
#         food = "Mutton Chaap"
#     else:
#         food = "Chole Bhature"
#     print("Kya main print ho payungi? :-(")
#     return food
# print("Lekin main toh pakka nahi print hounga :'(")
# print(menu("monday"))

# def numbers(n):
#     print(sum(n),"sum")
# numbers([2,2,3,0,7])

def numbers(*n):
    i=0
    sum=0
    while i<len(n):
        sum=sum+n[i]
        i=i+1
    print(sum)
numbers(98,6,78,23)


def func(*a):
    sum=0
    i=0
    while i<len(a):
        sum=sum+a[i]
        i=i+1
    print(sum)
func(2,3,8,7,4,5)