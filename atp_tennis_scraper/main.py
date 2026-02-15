import requests
from bs4 import BeautifulSoup


RANKINGS_URL = "https://www.atptour.com/en/rankings/singles"
PLAYER_API_URL = "https://www.atptour.com/en/-/www/players/hero/{player_id}?v=1"


def fetch_rankings_html():
    response = requests.get(RANKINGS_URL)
    response.raise_for_status()
    return response.text


def parse_rankings_html(html, limit=10):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="mega-table desktop-table non-live")

    if table is None:
        raise ValueError("Rankings table not found")

    tbody = table.find("tbody")
    trs = tbody.find_all("tr")

    return trs[:limit]


def fetch_player_details(player_id):
    url = PLAYER_API_URL.format(player_id=player_id)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_atp_rankings():
    html = fetch_rankings_html()
    trs = parse_rankings_html(html)

    players_data = []

    for tr in trs:
        rank = tr.find('td', class_='rank').text.strip()
        name = tr.find('li', class_='name center').find('span').text.strip()
        points = tr.find('td', class_='points').text.strip()

        a = tr.select_one("li.name.center a")
        profile_link = a["href"]

        player_id = profile_link.split("/")[-2]

        data = fetch_player_details(player_id)

        players_data.append({
            "Rank": rank,
            "Name": name,
            "Points": points,
            "Age": data.get("Age"),
            "Nationality": data.get("Nationality"),
        })

    return players_data



def display_top_10():
    top_players = fetch_atp_rankings()

    top_10_players = top_players[:10]

    
    print("\nTop 10 ATP Players:\n")
    for player in top_10_players:
        print(f"Rank: {player['Rank']}")
        print(f"Name: {player['Name']}")
        print(f"Points: {player['Points']}")
        print(f"Age: {player['Age']}")
        print(f"Nationality: {player['Nationality']}")
        print("-" * 40)


