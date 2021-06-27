#! /usr/bin/env python3

import json

tmp = [[]]

jsonFile = open("operations.json", 'r')

jsonData=json.load(jsonFile)

jsonFile.close()

# Перебор всех эелементов словаря,
# Нахождение нужных строк,
# Запись строк в список
for str in jsonData:
    if 'state' in str:
        if str['state'] == 'EXECUTED':
            date = str['date'].split('T')[0]
            descript = str['description']
            fromStr = str['from'] if 'from' in str else None
            if fromStr and fromStr.split()[0] == 'Cчет':
                fromStr=fromStr.split()[0]+'**'+fromStr[-4:]
            elif fromStr and fromStr.split()[0] != 'Cчет':
                fromStr=fromStr[:-16]+fromStr[-16:-12]+' '+fromStr[-12:-10]+'** **** '+fromStr[-4:]

            toStr = str['to'] if 'to' in str else None
            if toStr and toStr.split()[0] == 'Cчет':
                toStr=toStr.split()[0]+'**'+toStr[-4:]
            elif toStr and toStr.split()[0] != 'Cчет':
                toStr=toStr[:-16]+toStr[-16:-12]+' '+toStr[-12:-10]+'** **** '+toStr[-4:]

            amount=str['operationAmount']['amount']+' '+str['operationAmount']['currency']['name']

            tmp.append([date, descript, fromStr, toStr, amount])

# Удаление первого элемента списк так как он является пустым
tmp.pop(0)

# Сортировка списка по полю "Дата" от большей к меньшей
tmp.sort(key = lambda date: date[0], reverse=True)

# Перебор 5 первых элементов списка
for i in range(5):
    if tmp[i][2]:
        print("{0}.{1}.{2} {3}".format(tmp[i][0].split('-')[2], tmp[i][0].split('-')[1], tmp[i][0].split('-')[0], tmp[i][1]))
        print("{0} -> {1}".format(tmp[i][2], tmp[i][3]))
        print(tmp[i][4])
        print()
    else:
        print("{0}.{1}.{2} {3}".format(tmp[i][0].split('-')[2], tmp[i][0].split('-')[1], tmp[i][0].split('-')[0], tmp[i][1]))
        print(tmp[i][3])
        print(tmp[i][4])
        print()

exit()