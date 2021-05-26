def int_func(word):
    '''Пишем все слова с большой буквы'''
    all_words = []
    for i in word.split():
        i = i.capitalize()
        all_words.append(i)
    all_words = ' '.join(all_words)
    return all_words


my_str = (input('Введите слова: '))
print(int_func(my_str))
