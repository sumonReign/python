myString = "I love my country. Do you know the name of my country?"
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowels_count = []
for v in myString:
    if v in vowel:
     vowels_count.append(v)
print("the no. fo vowels in your string is: ", len(vowels_count)-1)