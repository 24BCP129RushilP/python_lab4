s=str(input("enter the string:"))

def toggle(word):
    toggle_word=""
    for letter in word:
        if (97<=ord(letter)<=122):
            toggle_word = toggle_word + chr(ord(letter) - 32)
        elif (65<=ord(letter)<=90):
            toggle_word = toggle_word + chr(ord(letter) + 32)
    return toggle_word

def UPPERCASE(word):
    upper_case=""
    for letter in word:
        if (97<=ord(letter)<=122):
            upper_case = upper_case + chr(ord(letter) - 32)
        else:
            upper_case = upper_case + letter 
    return upper_case
    
def lowercase(word):
    lower_case=""
    for letter in word:
        if (65<=ord(letter)<=90):
            lower_case = lower_case + chr(ord(letter) + 32)
        else:
            lower_case = lower_case + letter 
    return lower_case

print("TOGGLE CASE :",toggle(s))
print("UPPER CASE :",UPPERCASE(s))
print("LOWER CASE :",lowercase(s))

