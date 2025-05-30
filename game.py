import random
import os

# Define the playground size
playground_size = 100

# Function to print the playground
def print_playground(positions, traps, safes):
    playground_char = '_'
    os.system('cls' if os.name == 'nt' else 'clear')
    playground = [playground_char] * playground_size
    for trap in traps:
        playground[trap] = 'x'
    for safe in safes:
        playground[safe] = 'S'
    for i, pos in enumerate(positions):
        if playground[pos] == playground_char:
            playground[pos] = chr(65 + i)
        else:
            playground[pos] += chr(65 + i)
    print(''.join(playground))

# Get number of players
num_players = int(input("Enter the number of players: "))

# Initialize player positions
player_positions = [0] * num_players

# Randomly assign trap and safe spots
num_traps = 3
num_safes = 3
trap_spots = random.sample(range(1, playground_size - 1), num_traps)
safe_spots = random.sample(range(1, playground_size - 1), num_safes)

# Main game loop
current_player = 0
while all(pos < playground_size - 1 for pos in player_positions):
    input(f"Player {chr(65 + current_player)}, press Enter to roll the dice...")
    dice_roll = random.randint(1, 6)
    print(f"Player {chr(65 + current_player)} rolled a {dice_roll}!")

    player_positions[current_player] += dice_roll
    if player_positions[current_player] >= playground_size:
        player_positions[current_player] = playground_size - 1

    # Trap check (unless it's also a safe spot)
    if player_positions[current_player] in trap_spots and player_positions[current_player] not in safe_spots:
        print(f"Player {chr(65 + current_player)} landed on a trap! Back to start.")
        player_positions[current_player] = 0

    # Collision check
    for i in range(num_players):
        if i != current_player and player_positions[current_player] == player_positions[i]:
            print(f"Player {chr(65 + current_player)} landed on Player {chr(65 + i)}'s spot! Player {chr(65 + i)} goes back to start.")
            player_positions[i] = 0

    print_playground(player_positions, trap_spots, safe_spots)

    if dice_roll != 6:
        current_player = (current_player + 1) % num_players

winner = player_positions.index(max(player_positions))

print(f"🎉 Congratulations! Player {chr(65 + winner)} has reached the end of the playground.")
