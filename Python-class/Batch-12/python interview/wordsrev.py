def reverse_words(sentence):
    words = sentence.split(' ')
    print(words)
    reversed_sentence = ''
    for i in range(len(words)-1, -1, -1):
        reversed_sentence += words[i] + ' '
    return reversed_sentence.rstrip()
r=reverse_words("this is sample string")
print(r)
