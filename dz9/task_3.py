# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

f = open('test_file/task_3.txt', encoding='utf-8')
str0 = f.readlines()
sums = []
tmp_sum = 0
for i in str0:
    if i == "\n":
        sums.append(tmp_sum)
        tmp_sum = 0
    else:
       tmp_sum += int(i)
sums.sort()
three_most_expensive_purchases = sums[-1] + sums[-2] + sums[-3]

assert three_most_expensive_purchases == 202346
