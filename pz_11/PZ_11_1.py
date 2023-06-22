import random

n = 20  
numbers = [random.randint(-100, 100) for _ in range(n)]  

neg_odd = [num for num in numbers if num < 0 and num % 2 != 0]  
neg_odd_sum = sum(neg_odd) 
neg_odd_avg = neg_odd_sum / len(neg_odd) if neg_odd else 0  

with open('output.txt', 'w') as f:
    f.write('Исходные данные: {}\n'.format(numbers))
    f.write('Количество элементов: {}\n'.format(n))
    f.write('Отрицательные нечетные элементы: {}\n'.format(neg_odd))
    f.write('Сумма отрицательных нечетных элементов: {}\n'.format(neg_odd_sum))
    f.write('Среднее арифметическое отрицательных нечетных элементов: {:.2f}\n'.format(neg_odd_avg))
