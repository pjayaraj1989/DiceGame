import random
import os

# Define the playground size
playground_size = 1000

# Function to print the playground
def print_playground(positions, traps):
    os.system('cls' if os.name == 'nt' else 'clear')
    playground = ['_'] * playground_size
    for trap in traps:
        playground[trap] = 'x'
    for i, pos in enumerate(positions):
        if playground[pos] == '_':
            playground[pos] = chr(65 + i)  # A, B, C, ...
        else:
            playground[pos] += chr(65 + i)  # Multiple players on same spot
    print(''.join(playground))

# Get number of players
num_players = int(input("Enter the number of players: "))

# Initialize player positions
player_positions = [0] * num_players

# Randomly assign trap spots
num_traps = 3
trap_spots = random.sample(range(1, playground_size - 1), num_traps)

# Main game loop
current_player = 0
while all(pos < playground_size - 1 for pos in player_positions):
    input(f"Player {chr(65 + current_player)}, press Enter to roll the dice...")
    dice_roll = random.randint(1, 6)
    print(f"Player {chr(65 + current_player)} rolled a {dice_roll}!")

    player_positions[current_player] += dice_roll
    if player_positions[current_player] >= playground_size:
        player_positions[current_player] = playground_size - 1

    # Check for traps
    if player_positions[current_player] in trap_spots:
        print(f"Player {chr(65 + current_player)} landed on a trap! Back to start.")
        player_positions[current_player] = 0

    # Check if the current player lands on another player's spot
    for i in range(num_players):
        if i != current_player and player_positions[current_player] == player_positions[i]:
            print(f"Player {chr(65 + current_player)} landed on Player {chr(65 + i)}'s spot! Player {chr(65 + i)} goes back to start.")
            player_positions[i] = 0

    print_playground(player_positions, trap_spots)

    # If not a 6, switch player
    if dice_roll != 6:
        current_player = (current_player + 1) % num_players

print(f"🎉 Congratulations! Player {chr(65 + current_player)} has reached the end of the playground.")
