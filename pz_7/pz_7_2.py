open = ["[", "{", "("] # объявление вспомогательного массива с открывающимися скобками
close = ["]", "}", ")"] # объявление вспомогательного массива с закрывающимися скобками


def Check(str): # объявление функции
    stack = [] # объявление вспомогательного массива
    for i in str: # объявление цикла
        if i in open: 
            stack.append(i)
        elif i in close:
            pos = close.index(i)
            if stack and (open[pos] == stack[-1]):
                stack.pop()
            else:
                return 1 # вывод результата
    if len(stack) == 0:
        return 0 # вывод результата


print(Check(input('Введите строку '))) # вызов функции
