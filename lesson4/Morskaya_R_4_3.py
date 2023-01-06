#Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро. Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?




import requests
import json
import datetime as dt
import decimal as dc

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


response = requests.get(URL)

dict = json.loads(response.text)

def currency_rates(vlt):
    if dict.get('Valute').get(vlt.upper()):
        res = dict['Valute'][vlt.upper()]['Value']
        dttime = dt.datetime.fromisoformat(dict['Date']).date()
        print(f"Курс {vlt.upper()} на {dttime} равен {res}")
        print(dc.Decimal(res))
    else:
        print('None')


currency_rates('usd')
currency_rates('EUR')
currency_rates('sdf')


