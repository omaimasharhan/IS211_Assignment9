import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'data-test': 'historical-prices'})

    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:
            cells = row.find_all('td')

            if len(cells) >= 5:
                date = cells[0].get_text()
                close_price = cells[4].get_text()
                print(f"Date: {date}, Close Price: {close_price}")
            else:
                print("Insufficient data in the row.")
    else:
        print("Historical prices table not found.")
else:
    print("Failed to retrieve the web page.")