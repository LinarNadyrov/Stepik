# Задание 
# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, 
# удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]

# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# Функция не должна осуществлять ввод/вывод информации.

# Вариант 1:
def modify_list(l):
	lst2 = []
	for i in l:
		if i % 2 == 0:
			lst2.append(i // 2)
	l.clear()
	for i in lst2:
		l.append(i)

# Вариант 2:
def modify_list(l):
	a = len(l)
	b = []
	for i in range(0,a):
		if l[i] % 2 == 0:
			b.append(l[i] // 2)
	l.clear()
	for i in b:
		l.append(i)

# Проверка задания (робот) принял вариант №2. 
# Хотя на мой взгляд оба варианта достигают цели.

