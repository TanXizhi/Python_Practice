while True:
    word = input('Please enter a word:')
    if not word or word.isspace():
        break
    print('The word was', word)
