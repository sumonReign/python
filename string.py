song = 'cold, cold heart'

# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurrences of 'let'
print(song.replace('let', "don't let", 2))


song = 'cold, cold heart'
replaced_song = song.replace('o', 'e')

# The original string is unchanged
print('Original string:', song)

print('Replaced string:', replaced_song)

song = 'let it be, let it be, let it be'

# maximum of 0 substring is replaced
# returns copy of the original string
print(song.replace('let', 'so', 0))


myString = "My name is Sumon . This is a very common name but I feel proud of with my name"
print(myString.replace("name", "given name"))
