from bs4 import BeautifulSoup
import requests


def fetch_atp_rankings():

    # Fetch the HTML content from the ATP rankings page
    url = "https://www.atptour.com/en/rankings/singles"
    response = requests.get(url)
    html_content = response.content


    print("my tennis ")
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')



    # Extract the "table" element containing the rankings
    table = soup.find("table", class_="mega-table desktop-table non-live")

    # Extract the "tbody" element from the table
    tbody = table.find("tbody")

    #print(tbody)

    # Extract all "tr" (table row) elements inside "tbody"
    trs = tbody.find_all("tr")
    tre = tbody.find_all("ul", class_= 'player-stats')
    all_links = []
    for tr in tre:
    
        links = tr.find_all("a")  # Find all anchor tags in the current row
        for i in links:
            href = i.get('href')
            all_links.append(href)  # Add them to the list

    #print(all_links)



    # Extract all "tr" elements that have the class "lower-row"
    ltrs = tbody.find_all("tr", class_="lower-row")

    count = 0

    players_data = []

    for tr in trs:
        if count == 10:  # Limit to first 10 players
            break

        rank = tr.find('td', class_='rank').text.strip()
        name = tr.find('li', class_='name center').find('span').text.strip()
        points = tr.find('td', class_='points').text.strip()

        # Extract the player's ATP profile URL and get the player ID
        profile_url = "https://www.atptour.com" + all_links[count]
        player_id = profile_url.split('/')[-2]  # Extract player ID

        # Construct the API URL for player details
        api_url = "https://www.atptour.com/en/-/www/players/hero/"+player_id+"?v=1"

        response = requests.get(api_url)
        if response.status_code == 200:
        #  print(response.text)
            data = response.json()  # Convert response to JSON

            # Extract player details
            age = data.get("Age", "N/A")
            nationality = data.get("Nationality", "N/A")
            #rank = data.get("SglRank", "N/A")

            # Store player data in a dictionary
            player_info = {
                "Rank": rank,
                "Name": name,
                "Points": points,
                "Age": age,
                "Nationality": nationality,
            }

            # Append the player's data to the list
            players_data.append(player_info)

        count += 1



        
    for ltr in ltrs:

        profile_url = "https://www.atptour.com" + all_links[count]

        url = profile_url

        # Split the URL and get the second-to-last element
        player_id = url.split('/')[-2]

        api_url = "https://www.atptour.com/en/-/www/players/hero/"+player_id+"?v=1"


        rank = ltr.find('td', class_='rank').text.strip()
        
        # Extract name
        name = ltr.find('li', class_='name center').find('span').text.strip()
        
        # Extract points
        points = ltr.find('td', class_='points').text.strip()

        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()  # Convert response to JSON

            #Extract player information
            age = data.get("Age", "N/A")
            nationality = data.get("Nationality", "N/A")

            player_info = {
                "Rank": rank,
                "Name": name,
                "Points": points,
                "Age": age,
                "Nationality": nationality,
            }
            players_data.append(player_info)
        
        count += 1
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

display_top_10()
