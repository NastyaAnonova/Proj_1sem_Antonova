magnit = {'сахар', 'соль', 'молоко'}
pyterochka = {'молоко', 'мясо', 'сыр'}
print('Товары из магнита, отсутствующие в пятерочке:', magnit - pyterochka)
print('Товары из пятерочки, отсутсвующие в магните:', pyterochka - magnit)
print('Полный перечень всех товаров:', magnit|pyterochka)
print('Равны ли перечни товаров:', magnit == pyterochka)
