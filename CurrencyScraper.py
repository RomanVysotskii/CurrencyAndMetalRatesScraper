import requests
from fake_useragent import UserAgent
from lxml import etree
import csv

#Основные данные для запроса
ua = UserAgent()
url = 'https://www.cbr.ru/scripts/XML_daily.asp'
headers = {
    "Accept": "*/*",
    'User-Agent': ua.chrome
}

#Запрос
req = requests.get(url, headers=headers)

tree = etree.fromstring(req.content) #Передаём, как строку

#Парсинг и запись в файл
with open("currencies.csv", "w", encoding="utf-8-sig", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(["Code", "Name", "Price"])

    #Сохранение данных
    for valute in tree.findall(".//Valute"):
        name = valute.find("Name")
        value = valute.find("Value")
        nominal = valute.find("Nominal")
        code = valute.find("CharCode")
        price = float(value.text.replace(',', '.')) / int(nominal.text)
        price_str = f'="{price:.4f}"'
        writer.writerow([code.text, name.text, price_str]) #Запись в правильной последовательности