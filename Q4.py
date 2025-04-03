number=int(input("enter a number:"))

def CheckForPrime(n):
    for i in range(n):
        if n==1:
            print("nothing")
            break
        else:
            if n%i==0:
                print("is non prime")
                break
            else:
                continue

CheckForPrime(number)