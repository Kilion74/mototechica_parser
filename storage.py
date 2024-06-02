

print('Вуберите раздел: квадроциклы, электросамокаты...')
name = input().lower()
head = str
number = int
if name == 'квадроциклы':
    head = '/mototekhnika/kvadrotsikly/'
    number = 14
elif name == 'электросамокаты':
    head = '/aktivnyy-otdykh/elektrosamokaty/'
    number = 8
else:
    print('Введите корректные данные...')

print('Ведите название файла на английском...')
file_name = input()
