a = [10,0,5,'abc',3]
ab = [10,0,5,'abc',3,'ac', 1]

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
        of_a = int(a[b])
    except ValueError:
        print(f'ошибка с типом данных, {a[b]} не является числом')
        
        b = 0
        break
    b += 1


while b < len(ab):
    try:
        ab[b] = int('abc')
    except Exception as e:
        print(f'ошибка с типом данных, {e}')
        
        b = 0
        break
    b += 1

    
try:
    unvisible = a[-10]
except IndexError:
    print('Элемента с таким индексом не существует')
finally:
    print('проверка полностью завершена')
