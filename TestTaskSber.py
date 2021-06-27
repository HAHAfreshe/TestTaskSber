#! /usr/bin/env python3

import json


# p = 'Visa 1234123412341234'
# print(p[:-16]+p[-16:-12]+' '+p[-12:-10]+'** **** '+p[-4:])
# s = '12344321'
# print('**'+s[-4:])
class Main:
    def __init__(self):
        jsonFile = open("operations.json", 'r')

        jsonData=json.load(jsonFile)
        tmp=[[]]
        for s in jsonData:
            if 'id' in s:
                tmp.append([s['id'], s['date'].split('T')[0]])

        #tmp.sort(key=lambda i: i[1])
        print(tmp[1])
        # for s in jsonData:
        #     print(s)
        # for str in jsonData:
        #     if 'state' in str:
        #         if str['state'] == 'EXECUTED':
        #             date = str['date'].split('T')[0].split('-')
        #             descript = str['description']
        #             fromStr = str['from'] if 'from' in str else None
        #             if fromStr and fromStr.split()[0] == 'Cчет':
        #                 fromStr=fromStr.split()[0]+'**'+fromStr[-4:]
        #             elif fromStr and fromStr.split()[0] != 'Cчет':
        #                 fromStr=fromStr[:-16]+fromStr[-16:-12]+' '+fromStr[-12:-10]+'** **** '+fromStr[-4:]

        #             toStr = str['to'] if 'to' in str else None
        #             if toStr and toStr.split()[0] == 'Cчет':
        #                 toStr=toStr.split()[0]+'**'+toStr[-4:]
        #             elif toStr and toStr.split()[0] != 'Cчет':
        #                 toStr=toStr[:-16]+toStr[-16:-12]+' '+toStr[-12:-10]+'** **** '+toStr[-4:]
                    
        #             amount=str['operationAmount']['amount']
        #             curr=str['operationAmount']['currency']['name']

        #             print("{0}.{1}.{2} {3}".format(date[2], date[1], date[0], descript))
        #             print("{0} -> {1}".format(fromStr, toStr))
        #             print("{0} {1}".format(amount, curr))
        #             print()
        
        jsonFile.close()


if __name__ == '__main__':
    main=Main()


