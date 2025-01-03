import requests
import urllib.parse


def clean_battle_data(battle_data):
    # Define keys to retain
    desired_keys = {'name', 'level', 'elixirCost', 'rarity'}
    
    def filter_card_data(card):
        # Filter each card's data to retain only desired keys
        return {key: card[key] for key in card if key in desired_keys}

    def process_team_or_opponent(team_or_opponent):
        # Process each team or opponent's cards
        team_or_opponent['cards'] = [filter_card_data(card) for card in team_or_opponent['cards']]
        return team_or_opponent

    # Process the entire battle data
    for battle in battle_data:
        battle['team'] = [process_team_or_opponent(member) for member in battle['team']]
        battle['opponent'] = [process_team_or_opponent(member) for member in battle['opponent']]
    
    return battle_data

# Example usage with your JSON data
import json

# Assuming `battle_data` is your original JSON response loaded as a Python object
#cleaned_data = clean_battle_data(battle_data)

# Pretty-print the cleaned data
#print(json.dumps(cleaned_data, indent=2))

def get_player_data(player_tag, api_key):
    # URL-encode the player tag
    #encoded_tag = urllib.parse.quote(player_tag)
    
    # Define the API endpoint
    url = f'https://api.clashroyale.com/v1/players/{player_tag}/battlelog'
    
    # Set up the headers with the API key
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    # Make the GET request to the API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

# Example usage
if __name__ == '__main__':
    player_tag = '%232LGY9G'  # Replace with the actual player tag
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImRjMmRkNjkzLTVjYjUtNDRiZi05Yzg1LTFkYjNkZGZiZDMxMSIsImlhdCI6MTczNTkwMjI0Nywic3ViIjoiZGV2ZWxvcGVyLzliM2Y1ZTNlLTg5MzUtZWEzOC04MzkzLTAyNzlhOGI4MTFhOCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMDkuNTUuMTk3LjE1OCJdLCJ0eXBlIjoiY2xpZW50In1dfQ._o6CgsJOSfQ8I-6UAvDuvLZN5e6BJ71piMd-w8qg8EFcK5yDzDQEgDakX8N4kAeGoN4CwX4WN_WDf6fVLbcf1A'  # Replace with your Clash Royale API key
    player_data = get_player_data(player_tag, api_key)
    if player_data:
        #print(player_data)
        # Assuming `battle_data` is your original JSON response loaded as a Python object
        cleaned_data = clean_battle_data(player_data)

# Pretty-print the cleaned data
        print(json.dumps(cleaned_data, indent=2))


# TO RUN BEFORE python api-test0.py > outputCR.txt
