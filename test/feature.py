import pandas as pd
import json

# Dictionary mapping card names to IDs
cards_dict = {
    "Archers": 1,
    "Archer Queen": 2,
    "Arrows": 3,
    "Baby Dragon": 4,
    "Balloon": 5,
    "Bandit": 6,
    "Barbarians": 7,
    "Barbarian Barrel": 8,
    "Barbarian Hut": 9,
    "Bats": 10,
    "Battle Healer": 11,
    "Battle Ram": 12,
    "Bomber": 13,
    "Bomb Tower": 14,
    "Bowler": 15,
    "Bush Goblins": 16,
    "Cannon": 17,
    "Cannon Cart": 18,
    "Cursed Hog": 19,
    "Dark Prince": 20,
    "Dart Goblin": 21,
    "Defensive Buildings": 22,
    "Earthquake": 23,
    "Electro Dragon": 24,
    "Electro Giant": 25,
    "Electro Spirit": 26,
    "Electro Wizard": 27,
    "Elixir Blob": 28,
    "Elixir Collector": 29,
    "Elixir Golem": 30,
    "Elixir Golemite": 31,
    "Executioner": 32,
    "Fireball": 33,
    "Fire Spirit": 34,
    "Firecracker": 35,
    "Fisherman": 36,
    "Flying Machine": 37,
    "Freeze": 38,
    "Furnace": 39,
    "Giant": 40,
    "Giant Skeleton": 41,
    "Giant Snowball": 42,
    "Goblin Barrel": 43,
    "Goblin Brawler": 44,
    "Goblin Cage": 45,
    "Goblin Curse": 46,
    "Goblin Demolisher": 47,
    "Goblin Drill": 48,
    "Goblin Gang": 49,
    "Goblin Giant": 50,
    "Goblin Hut": 51,
    "Goblin Machine": 52,
    "Goblinstein": 53,
    "Goblins": 54,
    "Golden Knight": 55,
    "Golem": 56,
    "Golemite": 57,
    "Graveyard": 58,
    "Guardienne": 59,
    "Guards": 60,
    "Heal Spirit": 61,
    "Hog Rider": 62,
    "Hunter": 63,
    "Ice Golem": 64,
    "Ice Spirit": 65,
    "Ice Wizard": 66,
    "Inferno Dragon": 67,
    "Inferno Tower": 68,
    "Knight": 69,
    "Lava Hound": 70,
    "Lava Pup": 71,
    "Lightning": 72,
    "Little Prince": 73,
    "Log": 74,
    "Lumberjack": 75,
    "Magic Archer": 76,
    "Mega Knight": 77,
    "Mega Minion": 78,
    "Mighty Miner": 79,
    "Miner": 80,
    "Mini P.E.K.K.A.": 81,
    "Minion Horde": 82,
    "Minions": 83,
    "Monk": 84,
    "Monster": 85,
    "Mortar": 86,
    "Mother Witch": 87,
    "Musketeer": 88,
    "Night Witch": 89,
    "P.E.K.K.A.": 90,
    "Phoenix": 91,
    "Phoenix Egg": 92,
    "Poison": 93,
    "Prince": 94,
    "Princess": 95,
    "Ram Rider": 96,
    "Rage": 97,
    "Rascal Boy": 98,
    "Rascal Girl": 99,
    "Reborn Phoenix": 100,
    "Rocket": 101,
    "Royal Delivery": 102,
    "Royal Ghost": 103,
    "Royal Giant": 104,
    "Royal Hogs": 105,
    "Royal Recruits": 106,
    "Skeleton Army": 107,
    "Skeleton Barrel": 108,
    "Skeleton Dragons": 109,
    "Skeleton King": 110,
    "Skeletons": 111,
    "Sparky": 112,
    "Spear Goblins": 113,
    "Spawners": 114,
    "Suspicious Bush": 115,
    "Tesla": 116,
    "The Log": 117,
    "Three Musketeers": 118,
    "Tombstone": 119,
    "Tornado": 120,
    "Valkyrie": 121,
    "Void": 122,
    "Wall Breakers": 123,
    "Witch": 124,
    "Wizard": 125,
    "X-Bow": 126,
    "Zap": 127,
    "Zappies": 128
}

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
        deck = [cards_dict.get(card['name'], -1) for card in player['cards']]  # Convert names to IDs
        support_cards = [cards_dict.get(card['name'], -1) for card in player.get('supportCards', [])]
        trophy_change = player.get('trophyChange', 0) * (1 if is_team else -1)
        return {
            'Player Name': player['name'],
            **{f'Card {i+1}': card for i, card in enumerate(deck)},  # One column per card
            #'Support Cards': ', '.join(map(str, support_cards)),
            #'Trophy Change': trophy_change,
            #'Crowns': player['crowns']
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
