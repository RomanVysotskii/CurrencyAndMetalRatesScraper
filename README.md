# Currency and Metal Rates Scraper

Данный проект создан для портфолио.

Программа собирает с официального сайта Центрального банка РФ (https://www.cbr.ru) актуальную стоимость валют и драгоценных металлов.

Для работы используются:
- `fake-useragent` — для генерации случайных User-Agent заголовков при отправке HTTP-запросов
- `requests` — для получения HTML-страниц,
- `BeautifulSoup` (из библиотеки `beautifulsoup4`) — для парсинга и обработки данных,  
- в качестве парсера используется `lxml`.

Стоимость валют сохраняется в удобный CSV-файл, а стоимость металлов в txt-файл.

##Установка
git clone https://github.com/RomanVysotskii/CurrencyAndMetalRatesScraper
cd project
pip install -r requirements.txt
