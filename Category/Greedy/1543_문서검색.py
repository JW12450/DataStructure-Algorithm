sen = input()
word = input()

count = 0

while word in sen:
    count += 1
    word_start_index = sen.index(word)
    sen = sen[word_start_index+len(word):]
    #print(sen)


print(count)