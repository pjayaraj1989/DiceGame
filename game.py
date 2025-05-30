import random
import os
import time

# Define the playground size
playground_size = 100

# Function to print the playground
def print_playground(positions, traps, safes, last_dice_roll_status):
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
    print(last_dice_roll_status)

def animate_movement(positions, old_pos, current_player, traps, safes, last_dice_roll_status):
    temp_positions = positions.copy()
    for pos in range(old_pos, positions[current_player] + 1):
        temp_positions[current_player] = pos
        print_playground(temp_positions, traps, safes, last_dice_roll_status)
        time.sleep(0.2)  # Delay between each step

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
    input(f"\nPlayer {chr(65 + current_player)}, press Enter to roll the dice...")
    dice_roll = random.randint(1, 6)
    
    # Display dice outcome with ASCII art
    dice_art = {
        1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"
    }
    
    last_dice_roll_status = f"\n🎲 Player {chr(65 + current_player)} rolled: {dice_art[dice_roll]} ({dice_roll})"
    print(f"\n🎲 Player {chr(65 + current_player)} rolled: {dice_art[dice_roll]} ({dice_roll})")
    
    # Show current positions for all players
    print("\nPlayer Positions:")
    for i in range(num_players):
        print(f"Player {chr(65 + i)}: Position {player_positions[i]}", end="")
        if i == current_player:
            print(" (current player) 👈")
            #last_dice_roll_status += "\n (current player) 👈\n"
        else:
            print()

    #last_dice_roll_status = f"\n🎲 Player {chr(65 + current_player)} rolled: {dice_art[dice_roll]} ({dice_roll})"

    old_position = player_positions[current_player]
    player_positions[current_player] += dice_roll
    if player_positions[current_player] >= playground_size:
        player_positions[current_player] = playground_size - 1

    # Animate the movement
    animate_movement(player_positions, old_position, current_player, trap_spots, safe_spots, last_dice_roll_status)

    # Trap check (unless it's also a safe spot)
    if player_positions[current_player] in trap_spots and player_positions[current_player] not in safe_spots:
        print(f"Player {chr(65 + current_player)} landed on a trap! Back to start.")
        last_dice_roll_status += f"\nPlayer {chr(65 + current_player)} landed on a trap! Back to start.\n"
        time.sleep(1)  # Pause to show the trap landing
        player_positions[current_player] = 0
        print_playground(player_positions, trap_spots, safe_spots, last_dice_roll_status)

    # Collision check
    for i in range(num_players):
        if i != current_player and player_positions[current_player] == player_positions[i]:
            print(f"Player {chr(65 + current_player)} landed on Player {chr(65 + i)}'s spot! Player {chr(65 + i)} goes back to start.")
            last_dice_roll_status += f"\nPlayer {chr(65 + current_player)} landed on Player {chr(65 + i)}'s spot! Player {chr(65 + i)} goes back to start.\n"
            time.sleep(1)  # Pause to show the collision
            player_positions[i] = 0
            print_playground(player_positions, trap_spots, safe_spots, last_dice_roll_status)

    if dice_roll != 6:
        current_player = (current_player + 1) % num_players
    time.sleep(0.5)  # Small pause before next turn

winner = player_positions.index(max(player_positions))

print(f"🎉 Congratulations! Player {chr(65 + winner)} has reached the end of the playground.")
