s=str(input("enter the string:"))

def vowel_count(word):
    count=0
    vowel="AEIOUaeiou"
    for letter in word:
        if letter in vowel:
            count = count+1
    return count

print("no of vowels = ",vowel_count(s))