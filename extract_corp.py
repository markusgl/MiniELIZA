
with open('C:/Users/marku/Downloads/de-2012/de.txt', 'r', encoding='utf-8') as file:
    new_words = []
    for line in file:
        words = line.split()
        new_words.append(words[0])

    print(new_words)
with open('C:/Users/marku/develop/de_words_exported.txt', 'a', encoding='utf-8') as file:
    for word in new_words:
        file.write(word + " ")