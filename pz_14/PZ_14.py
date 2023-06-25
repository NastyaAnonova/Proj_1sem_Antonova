# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество 
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово 
# «произведение».

import re

files = open('writer.txt','r')
writer = files.read()
files.close()
print('Количество писателей в файле: ',len(re.findall('([А-Я].*)[А-Я].[А-Я].', writer)))
new_file = open('new_file.txt','w')
print(writer.replace('роман','произведение'),file=new_file)
new_file.close()
