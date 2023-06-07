# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


f = open('test_file/task1_data.txt', encoding='utf-8')
str0 = f.readlines()
str1 = ''.join(str0)
str2 = ''
index = ["0","1","2","3","4","5","6","7","8","9"]
for i in str1:
   if i not in index:
      str2 += i
l = open('test_file/task1_answer.txt', mode='w', encoding='utf-8')
l.write(str2)
l.close()
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')