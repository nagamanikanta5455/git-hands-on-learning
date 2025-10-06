sentence = "madam went to level the racecar"
for word in sentence.split():
    if word == word[::-1]:
        print(word)

