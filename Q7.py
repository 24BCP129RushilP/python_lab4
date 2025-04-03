n = int(input("Enter a number n: "))
r = int(input("Enter a number r: "))
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
print("nCr = ",(fact(n)) // (fact(n-r))*(fact(r)))
print("nPr = ",(fact(n)) // (fact(n-r)))
    

    