def func(speed):
    point=0
    num=int(input("enter the number"))
    if num==70:
        print("ok")
    elif num>=70:
        print("point =",1)
    elif num<=70 and num>=80:
        print("point =",2)
    elif point<=12:
        print("suspend")
        speed=speed+1
        point=point+1
func(70)