import random

def roll():
    dice = random.randint(1,6)
    return dice

while True:
    players = int(input("Enter the number of players (2-4) : "))
    if 2 <= players <=4:
        break
    else:
        print("Players must be in range (2-4)")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nplayer number",player_idx + 1, "has just started ")
        print("Your total score is: ",player_scores[player_idx],"\n")
        current_score = 0

        while True:
            dice_roll = input("would you like to roll (y/n): ").lower().strip()

            if dice_roll != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled 1! Turn over")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:",value )
                
            print("Your score is: ",current_score)
        
        player_scores[player_idx] += current_score
        print(f"Your total score is: {player_scores[player_idx]}")

max_score = max(player_scores)
winner = player_scores.index(max_score)
print(f"\nPlayer number {winner +1} is the winner with the score of: {max_score}")
            
    