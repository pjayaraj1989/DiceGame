import random

# Define the playground size
playground_size = 1000

# Function to print the playground
def print_playground(positions, traps):
    playground = ['_'] * playground_size
    for trap in traps:
        playground[trap] = 'T'
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
num_traps = 5
trap_spots = random.sample(range(1, playground_size - 1), num_traps)

# Main game loop
current_player = 0
while all(pos < playground_size - 1 for pos in player_positions):
    input(f"Player {current_player + 1}, press Enter to roll the dice...")
    dice_roll = random.randint(1, 6)
    print(f"Player {current_player + 1} rolled a {dice_roll}!")

    player_positions[current_player] += dice_roll
    if player_positions[current_player] >= playground_size:
        player_positions[current_player] = playground_size - 1

    # Check for traps
    if player_positions[current_player] in trap_spots:
        print(f"Player {current_player + 1} landed on a trap! Back to start.")
        player_positions[current_player] = 0

    print_playground(player_positions, trap_spots)

    # If not a 6, switch player
    if dice_roll != 6:
        current_player = (current_player + 1) % num_players

print(f"🎉 Congratulations! Player {current_player + 1} has reached the end of the playground.")
