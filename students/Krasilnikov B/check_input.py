# for letter in user_string:
#     if letter.isspace
try:
    user_string = input('введи какую нибудь строку')
except ValueError:
    print('Ошибка! В этой строке не должно быть ничего кроме букв!')
else:
    print(user_string.upper())
    try:
        n = int(input('введи индекс своей строки'))
        print(user_string[n])
    except IndexError:
        print('Вы ввели не существующий индекс!!!')
