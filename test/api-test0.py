import requests
import urllib.parse

def get_player_data(player_tag, api_key):
    # URL-encode the player tag
    encoded_tag = urllib.parse.quote(player_tag)
    
    # Define the API endpoint
    url = f'https://api.clashroyale.com/v1/players/{player_tag}'
    
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
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImJjMTg2ZmIwLTFjM2QtNDU1Mi1iYzZjLTU4MGFlNzJjYmM2NiIsImlhdCI6MTczNDk3MTQ3Mywic3ViIjoiZGV2ZWxvcGVyLzQzZmEzYzk2LWUyNjAtM2RlMi1mYzI5LWE1NGZkNmYxOTczMyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxOTMuMjA1LjIxMC44MyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.aT644TRkJTxfQVnHJmaK6d8g9VWKVcPkgWNANxmPCynEFbkH8W8UfnHcUZIQzAnFuNGT9pIErIRIS059eUZ5YA'  # Replace with your Clash Royale API key
    player_data = get_player_data(player_tag, api_key)
    if player_data:
        print(player_data)
