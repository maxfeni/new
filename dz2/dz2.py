import math

print("Задание №1")

side = float(input("Введите сторону квадрата: "))
perimeter = 4 * side
area = side ** 2
diagonal = round(side * 2 ** 0.5, 2)

print("Периметр квадрата:", perimeter)
print("Площадь квадрата:", area)
print("Диагональ квадрата:", diagonal)


print("Задание №2")  # первый вариант

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
d = b**2 - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(round(x1, 2))
    print(round(x2, 2))
elif d == 0:
    x1 = -b / (2 * a)
    print(round(x1, 2))
else:
    print('Нет корней')

print("Задание №2")  # второй вариант

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
d = b**2 - 4 * a * c

if d > 0:
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)
    print(round(x1, 2))
    print(round(x2, 2))
elif d == 0:
    x1 = -b / (2 * a)
    print(round(x1, 2))
else:
    print('Нет корней')


print("Задание №3")

str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

new_str = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]

print(new_str)


print("Задание №4")

file_path = input("Расположение файла: ")

a = (file_path.split("\\"))
file_name = a[-1].split('.')[0]  # не учтено, что файл может быть с "." в названии
disk = a[0][:-1]
folder = a[1]

print("Имя файла:", file_name)
print("Диск:", disk,)
print("Корневая папка:", folder)


print("Задание №5")

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

sum_str = f"{a} + {b} = {a + b}"
mult_str = f"{a} * {b} = {a * b}"

print(sum_str)
print(mult_str)


print("Задание №6")

string = input("Введите строку: ")
new_string = string[1::2]

print("Результат:", new_string)


print("Задание №7")  # первый вариант

sirst_string = "wtf"
second_string = "brick quz jmpy veldt whangs fox"

slice_start = second_string.find(first_string[1])
slice_end = second_string.find(first_string[2])
new_slice = second_string[slice_start:slice_end + 1]

print("Срез минимальной длины:", new_slice)

print("Задание №7")  # второй вариант

first_string = "wtf"
second_string = "brick quz jmpy veldt whangs fox"

slice_start = second_string.find(first_string[0])
slice_start2 = second_string.find(first_string[1])
slice_start3 = second_string.find(first_string[2])
sort = sorted([slice_start, slice_start2, slice_start3])
new_slice = second_string[sort[0]:sort[-1] + 1]
print("Срез минимальной длины:", new_slice)
