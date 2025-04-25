def capitalize(text):
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'

if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно')

if capitalize('') != '':
    raise Exception('Тест не выполнен')
print ('Тест пройден')