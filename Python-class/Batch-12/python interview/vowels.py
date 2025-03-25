def count_vowels(s):
    vowels = "aeiou"
    s = s.lower()
    v = 0
    c = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                v += 1
                
            else:
                c += 1
                
    return v, c
str=input("enter a string ")

v,c=count_vowels(str)
print("vowels",v)
print("consonants",c)
