"""Дан список размера N. Найти номера тех элементов списка, которые больше своего
правого соседа, и количество таких элементов. Найденные номера выводить в
порядке их возрастания.
"""
import random

result, a, n = list(), list(), list()


def _return_bool(ls):
    return ls[1]


try:
    for i in range(random.randint(3, 10)):
        n.append(random.randint(0, 100))
    for i in range(len(n) - 1):
        a.append(n[i] > n[i + 1])
    for i in list(filter(_return_bool, list(enumerate(a)))):
        result.append(i[0])
except Exception as e:
    print(f"Произошла ошибка - {str(e)}")

print(f"Номера - {result}, количество - {len(result)}")
