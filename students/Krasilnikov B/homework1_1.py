# Создаем список чисел от 1 до 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Используем list comprehension для фильтрации четных чисел
even_numbers = [num for num in numbers if num % 2 == 0]

# Выводим результат
print("Четные числа:", even_numbers)
