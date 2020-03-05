word = input('')
new_word = ''
vow ='aeyuioAEYUIO'

for letter in word:
    if letter not in vow:
        new_word += letter

print(new_word)