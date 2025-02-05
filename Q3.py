s1=str(input("enter the string:"))
s2=str(input("enter the string:"))

def check_str(l1,l2):
    if l1 in l2:
        print("s1 is in s2")
    else:
        print("l1 is not in l2")

check_str(s1,s2)
