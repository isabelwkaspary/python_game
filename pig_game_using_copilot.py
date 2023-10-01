import random

def roll(): 
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("How many players? (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4.")
    else:
        print("Please enter a valid number.")

max_score = 50
player_scores = [0 for _ in range(players)]
player_idx = -1

while max(player_scores) < max_score:
    player_idx = (player_idx + 1) % players
    print("\nIt is player", player_idx + 1, "'s turn!\n")
    print("Your current score is:", player_scores[player_idx],"\n")
    current_score = 0

    while True:
        should_roll = input("Would you like to roll? (y/n): ")
        if should_roll.lower() != "y":
            break

        value = roll()
        if value == 1:
            print("You rolled a 1. Your turn is over.")
            current_score = 0
            break
        else:
            current_score += value
            print("You rolled a:", value)

        print("Your current score is:", current_score)

    player_scores[player_idx] += current_score
    print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player", winning_idx + 1, "wins with a total score of:", max_score)
