# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import string
import random

def generate_random_name(start, end=None):
    if end is None:
        start, end = 0, start
    while start < end:
        str1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 15)))
        str2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 15)))
        yield str1 + ' ' + str2
        start += 1


gen = generate_random_name(1, 5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))