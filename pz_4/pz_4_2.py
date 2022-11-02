while True:
    try:
        A, B, C = int(input('Введите A: ')), int(input('Введите B: ')), int(input('Введите C: ')), # Ввод числа
        if A > 0 and B > 0 and C > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print("Некорректный ввод, попробуйте еще раз!")

n_A = 0
while A >= C:
    A -= C
    n_A += 1

n_B = 0
while B >= C:
    B -= C
    n_B += 1

k = 0
i = 0
while i < n_A:
    i += 1
    j = 0
    while j < n_B:
        j += 1
        k += 1

print("Количество квадратов на прямоугольнике:", k)