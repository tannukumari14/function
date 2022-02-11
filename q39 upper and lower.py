def func(s):
    upper_case=0
    lower_case=0
    c=0
    for c in s:
        if c.isupper():
            upper_case+=1
        elif c.islower():
            lower_case+=1
        else:
            pass
    print("original_string",s)
    print("no of lower case",lower_case)
    print("no of upper case",upper_case)
func("The Red Bull")

