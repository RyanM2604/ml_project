from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'my-app'}
response = requests.get("https://finviz.com/quote.ashx?t=GOOG&p=d", headers=headers)
soup = BeautifulSoup(response.content, 'lxml')

table_rows = soup.find_all('tr', class_='cursor-pointer has-label')

titles = []

for data in table_rows:
    titles.append(data.find('a', class_='tab-link-news').text)

print(titles)