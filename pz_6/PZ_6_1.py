"""Сформировать и вывести целочисленный список размера 10, содержащий 10 первых
положительных нечетных чисел: 1,3,5, ...."""

result = []
n = 0

try:
    while n < 20:
        result.append(n) if n % 2 != 0 else None
        n += 1
except Exception as e:
    print(f'Произошла ошибка - {str(e)}')

print(result)