import cah

# Create a new game with the family-friendly deck
game = cah.new_game("family")

# Start a new round
game.start_round()

# Get the black card for the round
black_card = game.black_card

# Print the black card prompt
print(black_card.prompt)

# Get the white cards for the round
white_cards = game.get_white_cards()

# Print the white cards
for i, card in enumerate(white_cards):
    print(f"{i+1}. {card}")

# Allow players to select a white card
selected_card_index = int(input("Select a card: "))-1

# Submit the selected card as the answer for the round
game.submit_white_card(white_cards[selected_card_index])

# Get the winning card and player
winning_card, winning_player = game.get_winning_card_and_player()

# Print the winning card and player
print(f"The winning card is {winning_card} submitted by {winning_player}")
