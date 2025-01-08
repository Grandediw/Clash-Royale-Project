import requests
from bs4 import BeautifulSoup
# Base URL for raw GitHub images
base_url = "https://raw.githubusercontent.com/RoyaleAPI/cr-api-assets/master/cards/"


# Predefined card_numbers dictionary
card_numbers = {
    "Archers": 1, "Archer Queen": 2, "Baby Dragon": 3, "Balloon": 4, "Bandit": 5, "Barbarians": 6,
    "Bats": 7, "Battle Healer": 8, "Battle Ram": 9, "Bomber": 10, "Bowler": 11, "Bush Goblins": 12,
    "Cannon Cart": 13, "Cursed Hog": 14, "Dark Prince": 15, "Dart Goblin": 16, "Electro Dragon": 17,
    "Electro Giant": 18, "Electro Spirit": 19, "Electro Wizard": 20, "Elite Barbarians": 21,
    "Elixir Blob": 22, "Elixir Golem": 23, "Elixir Golemite": 24, "Executioner": 25, "Firecracker": 26,
    "Fire Spirit": 27, "Fisherman": 28, "Flying Machine": 29, "Giant": 30, "Giant Skeleton": 31,
    "Goblin Brawler": 32, "Goblin Gang": 33, "Goblin Demolisher": 34, "Goblin Giant": 35,
    "Goblin Machine": 36, "Goblins": 37, "Goblinstein": 38, "Golden Knight": 39, "Golem": 40,
    "Golemite": 41, "Guardienne": 42, "Guards": 43, "Hog Rider": 44, "Hunter": 45, "Heal Spirit": 46,
    "Ice Golem": 47, "Ice Spirit": 48, "Ice Wizard": 49, "Inferno Dragon": 50, "Knight": 51,
    "Lava Hound": 52, "Lava Pup": 53, "Little Prince": 54, "Lumberjack": 55, "Magic Archer": 56,
    "Mega Knight": 57, "Mega Minion": 58, "Mighty Miner": 59, "Miner": 60, "Mini P.E.K.K.A.": 61,
    "Minion Horde": 62, "Minions": 63, "Monk": 64, "Mother Witch": 65, "Monster": 66, "Musketeer": 67,
    "Night Witch": 68, "P.E.K.K.A.": 69, "Phoenix": 70, "Reborn Phoenix": 71, "Prince": 72,
    "Princess": 73, "Ram Rider": 74, "Rascal Boy": 75, "Rascal Girl": 76, "Royal Ghost": 77,
    "Royal Giant": 78, "Royal Hogs": 79, "Royal Recruits": 80, "Skeleton Army": 81,
    "Skeleton Barrel": 82, "Skeleton Dragons": 83, "Skeleton King": 84, "Skeletons": 85, "Sparky": 86,
    "Spear Goblins": 87, "Suspicious Bush": 88, "Three Musketeers": 89, "Valkyrie": 90,
    "Wall Breakers": 91, "Witch": 92, "Wizard": 93, "Zappies": 94,"Bomb Tower": 95, "Cannon": 96, "Cannon Cart (broken)": 97, "Inferno Tower": 98, "Mortar": 99,
        "Tesla": 100, "X-Bow": 101,"Barbarian Hut": 102, "Elixir Collector": 103, "Furnace": 104, "Goblin Cage": 105,
        "Goblin Drill": 106, "Goblin Hut": 107, "Phoenix Egg": 108, "Tombstone": 109, "Arrows": 110, "Barbarian Barrel": 111, "Earthquake": 112, "Fireball": 113, "Freeze": 114,
        "Giant Snowball": 115, "Goblin Curse": 116, "Lightning": 117, "Poison": 118, "Rage": 119, "Rocket": 120, "Royal Delivery": 121, "The Log": 122, "Tornado": 123, "Void": 124, "Zap": 125,
        "Barbarian Barrel": 126, "Barbarian Hut": 127, "Battle Ram": 128, "Elixir Golem": 129,
        "Elixir Golemite": 130, "Furnace": 131, "Goblin Barrel": 132, "Goblin Cage": 133, "Goblin Curse": 134,
        "Goblin Drill": 135, "Goblin Giant": 136, "Goblin Hut": 137, "Golem": 138, "Graveyard": 139,
        "Lava Hound": 140, "Little Prince": 141, "Mother Witch": 142, "Night Witch": 143,
        "Phoenix Egg": 144, "Royal Delivery": 145, "Skeleton Barrel": 146, "Skeleton King": 147,
        "Suspicious Bush": 148, "Tombstone": 149, "Witch": 150,
        "Archers/Evolution": 155, "Barbarians/Evolution": 156, "Battle Ram/Evolution": 157,
        "Bats/Evolution": 158, "Bomber/Evolution": 159, "Cannon/Evolution": 160,
        "Electro Dragon/Evolution": 161, "Firecracker/Evolution": 162, "Giant Snowball/Evolution": 163,
        "Goblin Barrel/Evolution": 164, "Goblin Cage/Evolution": 165, "Goblin Drill/Evolution": 166,
        "Goblin Giant/Evolution": 167, "Ice Spirit/Evolution": 168, "Knight/Evolution": 169,
        "Mega Knight/Evolution": 170, "Mortar/Evolution": 171, "Musketeer/Evolution": 172,
        "P.E.K.K.A/Evolution": 173, "Royal Giant/Evolution": 174, "Royal Recruits/Evolution": 175,
        "Skeletons/Evolution": 176, "Tesla/Evolution": 177, "Valkyrie/Evolution": 178,
        "Wall Breakers/Evolution": 179, "Wizard/Evolution": 180, "Zap/Evolution": 181

}

# Normalize card names and generate the full URLs
card_images = {
    card_name: f"{base_url}{card_name.lower().replace(' ', '-').replace('/', '-').replace('.', '')}.png"
    for card_name in card_numbers.keys()
}

# Print the resulting card_images dictionary
for card, url in card_images.items():
    print(f'"{card}": "{url}",')