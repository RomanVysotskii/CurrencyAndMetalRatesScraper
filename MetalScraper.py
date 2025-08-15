import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import date

#Основные данные для запроса
ua = UserAgent()
url = 'https://www.cbr.ru/hd_base/metall/metall_base_new?'
headers = {
    "Accept": "*/*",
    'User-Agent': ua.chrome
}

#Запрос
req = requests.get(url, headers=headers)

today = ".".join(str(date.today()).split("-")[::-1]) #Сегодняшняя дата

#Парсинг
soup = BeautifulSoup(req.text, 'lxml')

blocks = soup.find_all("tr")

for block in blocks:
    date = block.find("td")
    if date:
        date = date.text

    if date == today:
        tds = block.find_all("td")
        values = [td.text for td in tds]
        break
    else:
        continue

values = values[1:]

#Запись в файл
with open("metals.txt", "w", encoding="utf-8") as f:
    f.write("(руб/грамм) \n")
    f.write(f"На {today}: \n")
    f.write(f"Золото - {values[0]}\n")
    f.write(f"Серебро - {values[1]}\n")
    f.write(f"Платина - {values[2]}\n")
    f.write(f"Палладий - {values[3]}\n")

