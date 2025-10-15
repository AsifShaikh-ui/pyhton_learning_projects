import random

def roll():
    dice = random.randint(1,6)
    print(dice)

while True:
    players = int(input("Enter the number of players (2-4) : "))
    if 2 <= players <=4:
        break
    else:
        print("Players must be in range (2-4)")

max_score = 30
player_scores = [0 for _ in range(players)]
print(player_scores)