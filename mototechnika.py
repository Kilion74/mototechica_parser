import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
import csv

# pip install lxml
while True:
    print('Выберите раздел: квадроциклы, электросамокаты...')
    name = input().lower()
    url_name = str
    number = int
    if name == 'квадроциклы':
        url_name = '/mototekhnika/kvadrotsikly/'
        number = 14
    elif name == 'электросамокаты':
        url_name = '/aktivnyy-otdykh/elektrosamokaty/'
        number = 8
    else:
        print('Введите корректные данные...')

    print('Ведите название файла на английском...')
    file_name = input()
    count = 1
    while count <= number:
        print(number)
        print(url_name)
        url = f'https://globaldrive.ru/novokuybyshevsk/catalog{url_name}?view=list&CF_CACHE_BITRIX_SM_ARG_CITY=1&_CF_CACHE_MOBILE=0&PAGEN_1={count}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        data = requests.get(url, headers=headers).text
        block = BeautifulSoup(data, 'lxml')
        # print(block)
        heads = block.find_all('div', class_='catalog-list__item')
        print(len(heads))
        for i in heads:
            w = i.find_next('a', href=True)

            get_url = ('https://globaldrive.ru' + w['href'])
            cloon = requests.get(get_url, headers=headers).text
            cpouk = BeautifulSoup(cloon, 'lxml')
            name = cpouk.find('div', class_='card__title')
            print(name.text.strip())
            head = (name.text.strip())
            price = cpouk.find('div', class_="card-info__cur-price")
            try:
                print(price.text.strip())
                cena = (price.text.strip())
            except:
                print('None')
                cena = 'none'
            pixx = cpouk.find('div', class_='picture-lg__inner').find('a', href=True)
            print('https://globaldrive.ru' + pixx['href'])
            photo = ('https://globaldrive.ru' + pixx['href'])
            param_1 = cpouk.find_all('ul', class_='tab-props__list')
            charr = (param_1[0].find_all_next('li'))
            print(' '.join(charr[0].text.strip().replace('?', ':').split()))
            xaract_1 = (' '.join(charr[0].text.strip().replace('?', ':').split()))
            print(' '.join(charr[1].text.strip().replace('?', ':').split()))
            xaract_2 = (' '.join(charr[1].text.strip().replace('?', ':').split()))
            print(' '.join(charr[2].text.strip().replace('?', ':').split()))
            xaract_3 = (' '.join(charr[2].text.strip().replace('?', ':').split()))
            print(' '.join(charr[3].text.strip().replace('?', ':').split()))
            xaract_4 = (' '.join(charr[3].text.strip().replace('?', ':').split()))
            print(' '.join(charr[4].text.strip().replace('?', ':').split()))
            xaract_5 = (' '.join(charr[4].text.strip().replace('?', ':').split()))
            print(' '.join(charr[5].text.strip().replace('?', ':').split()))
            xaract_6 = (' '.join(charr[5].text.strip().replace('?', ':').split()))

            param_2 = cpouk.find_all('ul', class_='tab-props__list')
            charr = (param_2[1].find_all_next('li'))
            print(' '.join(charr[0].text.strip().replace('?', ':').split()))
            xaract_7 = (' '.join(charr[0].text.strip().replace('?', ':').split()))
            print(' '.join(charr[1].text.strip().replace('?', ':').split()))
            xaract_8 = (' '.join(charr[1].text.strip().replace('?', ':').split()))
            print(' '.join(charr[2].text.strip().replace('?', ':').split()))
            xaract_9 = (' '.join(charr[2].text.strip().replace('?', ':').split()))
            print(' '.join(charr[3].text.strip().replace('?', ':').split()))
            xaract_10 = (' '.join(charr[3].text.strip().replace('?', ':').split()))

            param_3 = cpouk.find_all('ul', class_='tab-props__list')
            charr = (param_3[2].find_all_next('li'))
            print(' '.join(charr[0].text.strip().replace('?', ':').split()))
            xaract_11 = (' '.join(charr[0].text.strip().replace('?', ':').split()))

            param_4 = cpouk.find_all('ul', class_='tab-props__list')
            charr = (param_4[3].find_all_next('li'))
            print(' '.join(charr[0].text.strip().replace('?', ':').split()))
            xaract_12 = (' '.join(charr[0].text.strip().replace('?', ':').split()))
            print(' '.join(charr[1].text.strip().replace('?', ':').split()))
            xaract_13 = (' '.join(charr[1].text.strip().replace('?', ':').split()))
            print(' '.join(charr[2].text.strip().replace('?', ':').split()))
            xaract_14 = (' '.join(charr[2].text.strip().replace('?', ':').split()))
            print(' '.join(charr[3].text.strip().replace('?', ':').split()))
            xaract_15 = (' '.join(charr[3].text.strip().replace('?', ':').split()))

            param_5 = cpouk.find_all('ul', class_='tab-props__list')
            charr = (param_5[4].find_all_next('li'))
            print(' '.join(charr[0].text.strip().replace('?', ':').split()))
            xaract_16 = (' '.join(charr[0].text.strip().replace('?', ':').split()))
            print(' '.join(charr[1].text.strip().replace('?', ':').split()))
            xaract_17 = (' '.join(charr[1].text.strip().replace('?', ':').split()))
            print(' '.join(charr[2].text.strip().replace('?', ':').split()))
            xaract_18 = (' '.join(charr[2].text.strip().replace('?', ':').split()))
            print(' '.join(charr[3].text.strip().replace('?', ':').split()))
            xaract_19 = (' '.join(charr[3].text.strip().replace('?', ':').split()))
            print(' '.join(charr[4].text.strip().replace('?', ':').split()))
            xaract_20 = (' '.join(charr[4].text.strip().replace('?', ':').split()))
            print(' '.join(charr[5].text.strip().replace('?', ':').split()))
            xaract_21 = (' '.join(charr[5].text.strip().replace('?', ':').split()))
            print(' '.join(charr[6].text.strip().replace('?', ':').split()))
            xaract_22 = (' '.join(charr[6].text.strip().replace('?', ':').split()))
            print('\n')

            storage = {'name': head, 'price': cena, 'url': get_url, 'photo': photo, 'param_1': xaract_1,
                       'param_2': xaract_2, 'param_3': xaract_3, 'param_4': xaract_4, 'param_5': xaract_5,
                       'param_6': xaract_6,
                       'param_7': xaract_7, 'param_8': xaract_8, 'param_9': xaract_9, 'param_10': xaract_10,
                       'param_11': xaract_11, 'param_12': xaract_12, 'param_13': xaract_13, 'param_14': xaract_14,
                       'param_15': xaract_15, 'param_16': xaract_16, 'param_17': xaract_17, 'param_18': xaract_18,
                       'param_19': xaract_19, 'param_20': xaract_20, 'param_21': xaract_21, 'param_22': xaract_22}

            fields = ['Name', 'Price', 'URL', 'Photo', 'Param_1', 'Param_2', 'Param_3', 'Param_4', 'Param_5', 'Param_6',
                      'Param_7', 'Param_8', 'Param_9', 'Param_10', 'Param_11', 'Param_12', 'Param_13', 'Param_14',
                      'Param_15',
                      'Param_16', 'Param_17', 'Param_18', 'Param_19', 'Param_20', 'Param_21', 'Param_22']
            with open(f'{file_name}.csv', 'a+', encoding='utf-16') as file:
                pisar = csv.writer(file, delimiter=';', lineterminator='\r')
                # Проверяем, находится ли файл в начале и пуст ли
                file.seek(0)
                if len(file.read()) == 0:
                    pisar.writerow(fields)  # Записываем заголовки, только если файл пуст
                pisar.writerow([storage['name'], storage['price'], storage['url'], storage['photo'], storage['param_1'],
                                storage['param_2'], storage['param_3'], storage['param_4'], storage['param_5'],
                                storage['param_6'], storage['param_7'], storage['param_8'], storage['param_9'],
                                storage['param_10'], storage['param_11'], storage['param_12'], storage['param_13'],
                                storage['param_14'], storage['param_15'], storage['param_16'], storage['param_17'],
                                storage['param_18'], storage['param_19'], storage['param_20'], storage['param_21'],
                                storage['param_22']])
        count += 1
