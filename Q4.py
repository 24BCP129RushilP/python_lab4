str1 = input("Enter the string 1: ")
str2 = input("Enter the string 2 (string to remove): ")

def remove_string(s1,s2):
    return s1.replace(s2, "")

print("Updated string:", remove_string(str1, str2))