import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the list of cards from the provided URL
url = 'https://clashroyale.fandom.com/wiki/Cards'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 2: Extract card names from the webpage
# Note: The actual HTML structure of the page may vary; adjust the selectors accordingly
card_elements = soup.select('div.card-list a.card-link')  # Example selector
card_names = [card.get_text().strip() for card in card_elements]

# Step 3: Sort the card names alphabetically
card_names_sorted = sorted(card_names)

# Step 4: Assign numeric IDs to each card
card_to_id = {card: idx + 1 for idx, card in enumerate(card_names_sorted)}
id_to_card = {idx + 1: card for idx, card in enumerate(card_names_sorted)}

# Display the mappings
print("Card to ID Mapping:")
for card, id in card_to_id.items():
    print(f"{card}: {id}")

print("\nID to Card Mapping:")
for id, card in id_to_card.items():
    print(f"{id}: {card}")
