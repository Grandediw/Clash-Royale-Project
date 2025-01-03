import pandas as pd
import json

# Assuming the provided JSON is saved in 'outputCR.json'
try:
    with open('outputCR.json', 'r', encoding='utf-16') as f:
        battle_data = json.load(f)  # Load the JSON data
except FileNotFoundError:
    print("File not found. Ensure 'outputCR.json' exists in the directory.")
    battle_data = None
except json.JSONDecodeError as e:
    print(f"Invalid JSON format: {e}")
    battle_data = None

if battle_data:
    # Function to process a single player's data
    def process_player_data(player, is_team=True):
        deck = [card['name'] for card in player['cards']]
        support_cards = [card['name'] for card in player.get('supportCards', [])]
        #trophy_change = player.get('trophyChange', 0) * (1 if is_team else -1)
        return {
            'Player Name': player['name'],
            'Deck': ', '.join(deck),
            'Support Cards': ', '.join(support_cards),
            #'Trophy Change': trophy_change,
            'Crowns': player['crowns']
        }

    # Collect all matches
    all_matches = []

    for match in battle_data:
        team = match['team'][0]
        opponent = match['opponent'][0]
        team_data = process_player_data(team, is_team=True)
        opponent_data = process_player_data(opponent, is_team=False)

        # Add Win or Lose based on crowns
        if team['crowns'] > opponent['crowns']:
            team_data['Result'] = 'WIN'
            opponent_data['Result'] = 'LOSE'
        elif team['crowns'] < opponent['crowns']:
            team_data['Result'] = 'LOSE'
            opponent_data['Result'] = 'WIN'
        else:
            team_data['Result'] = 'DRAW'
            opponent_data['Result'] = 'DRAW'

        all_matches.append(team_data)
        all_matches.append(opponent_data)

    # Create the DataFrame
    df = pd.DataFrame(all_matches)

    # Display the DataFrame
    print(df)
else:
    print("No battle data available.")
