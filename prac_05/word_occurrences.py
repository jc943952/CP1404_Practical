text = input('please enter a sentence:')
words = text.split()
words_to_count = {}

for word in words:
    word = word.lower()

    if word in words_to_count:
        words_to_count[word] += 1
    else:
        words_to_count[word] = 1

for word in sorted(words_to_count):
    print(f'{word}: {words_to_count[word]}')
