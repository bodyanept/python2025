a = [10,0,5,'abc',3]

b = 0


while b < len(a):
    try:
       res = a[b + 1] / a[b]
    except ZeroDivisionError:
        print('Ошибка деления на ноль')
        b = 0
        break
    b += 1

while b < len(a):
    try:
        # of_a = int(a[b])
        of_a = bool('asdf')
    except TypeError:
        print(f'ошибка с типом данных, {a[b]} не является числом')
        
        b = 0
        break
    b += 1

    
try:
    unvisible = a[-10]
except IndexError:
    print('Элемента с таким индексом не существует')
finally:
    print('проверка полностью завершена')
