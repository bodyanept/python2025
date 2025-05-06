import random


x = [random.randint(0, 100) for _ in range(10)]


def bogosort(x):
    print(f'Изначальный вид списка: {x}')
    n = len(x)
    while True:
        
        y = random.shuffle(x)
        print(f'Перемешанный вид списка: {y}')
        for i in range(n - 1):
            if x[i] < x[i + 1]:
                continue
            else:
                print('список не отсортирован')
                break
            
            print(f'Список {x} отсортирован')
            
bogosort(x)
