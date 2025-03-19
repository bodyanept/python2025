try:
    user_string = input('введи какую нибудь строку')
    for letter in user_string:
        if not(letter.isalpha() and letter.isascii()) and letter !=' ':
            raise ValueError('Ошибка! В этой строке не должно быть ничего кроме латинских букв и пробелов!!!')
except ValueError:
    print('Ошибка! В этой строке не должно быть ничего кроме букв!')
else:
    print(f'Преобрахованная строка: {user_string.upper()}')
    try:
        n = input('введи индекс своей строки')
        if not n.isdigit():
            raise TypeError('Индекс должен быть целым числом.')
    except TypeError as e:
        print(f'Ошибка: {e}')
    else:
        try:
            i = int(n)
            print(f'символ на позиции {i}: {user_string[i]}')
        except IndexError:
            print('Вы ввели не существующий индекс!!!')




