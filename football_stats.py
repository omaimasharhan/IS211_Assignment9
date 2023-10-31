import requests
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"
response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    data_container = soup.find('div', {'class': 'TableBase'})

    if data_container:
        stats_table = data_container.find('table')

        if stats_table:
            for row in stats_table.find_all('tr')[1:21]:
                cells = row.find_all('td')
                player_name = cells[0].get_text()
                player_position = cells[1].get_text()
                player_team = cells[2].get_text()
                player_touchdowns = cells[3].get_text()
                print(f"Player: {player_name}, Position: {player_position}, Team: {player_team}, Touchdowns: {player_touchdowns}")
        else:
            print("Player statistics table not found.")
    else:
        print("Data container not found.")
else:
    print("Failed to retrieve the web page.")
