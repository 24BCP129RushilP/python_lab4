s=str(input("enter a alphanumeric string:"))

Numeric = "0123456789"
Alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def count(word):
    num_cou=0
    alp_cou=0
    for item in word:
        if item in Numeric: num_cou+=1
        elif item in Alpha: alp_cou+=1
    print("ALPABET COUNT:",alp_cou,"NUMERIC COUNT:",num_cou)

count(s)