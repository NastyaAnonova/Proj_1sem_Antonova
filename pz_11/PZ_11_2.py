# Из предложенного текстового файла (text18-1.txt) вывести на экран его содержимое, количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив последнюю строку между первой и второй.

with open('text18-1.txt', 'r') as file:
    content = file.read()
    print(content)
    upper_count = sum(1 for c in content if c.isupper())

print(f'Количество букв в верхнем регистре: {upper_count}')

with open('text18-1.txt', 'r') as file:
    lines = file.readlines()

with open('poem.txt', 'w') as f:
    
    f.write(lines[0] + '\n')
    
    f.write(lines[-1] + '\n')
    
    for line in lines[1:-1]:
        f.write('\t' + line + '\n')
