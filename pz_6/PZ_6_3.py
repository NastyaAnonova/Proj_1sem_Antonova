"""Дан список А размера N и целые числа К и L. (1<К < L < N). Переставить в обратном
порядке элементы списка, расположенные между элементами Ак и Al, не включая
эти элементы."""
import random

def check(s):
    num = input(s)
    while type(num) != int:
        try:
            return int(num)
        except ValueError:
            print("Введи число снова!")
        num = input(s)

a = []

for i in range(random.randint(5, 10)):
    a.append(random.randint(0, 100))
print(a)
l, k = check(f"Введите пожалуйста число, меньшее {len(a)}: "), check(
    "Введите пожалуйста число, меньшее прошлого числа: ")


print(list(reversed(a[k:l])))
