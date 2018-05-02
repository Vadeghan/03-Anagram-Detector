#Made by Marika Colby (12.10)

def is_anagram(first, second):
    return sorted(str(first)) == sorted(str(second))


print(is_anagram("anagram", "nagaram")) #True
print(is_anagram("green", "egern"))     #True
print(is_anagram("abcd", "abcd"))       #True
print(is_anagram("egg", "bacon"))       #False


#Extension:

print(is_anagram(123967, 723916))       #True
print(is_anagram(192745, "921574"))     #True
print(is_anagram(9814, 2359772))        #False
print(is_anagram(25982, 2345))          #False
print(is_anagram("235972", 52208285))   #False
