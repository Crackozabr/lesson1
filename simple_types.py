v = input('Введите число от 1 до 10: ')
v = int(v) + 10
print(v) 
# поправьте код, чтобы выводилось число
# на 10 больше, чем введённое
# например, пользователь ввел 10 
# программа вывела 20

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?') # поправьте код, чтобы выводилась строка
 			# Привет, ИМЯ! Как дела?

# Выведите на экран при помощи print() результат работы:
print(float('1'))  # 1.0
print(int('2.5'))  # ValueError: invalid literal for int() with base 10: '2.5'
print(bool(1))  # True
print(bool(''))  # False
print(bool(0))  # False