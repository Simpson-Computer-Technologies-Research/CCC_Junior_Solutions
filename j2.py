# Get the amount of players
players: int = int(input())

res: int = 0
for _ in range(players):
    # // Get the inputted points and fouls
    points: int = int(input())
    fouls: int = int(input())

    # // If total points - fouls is greater than 40
    if (points*5) - (fouls*3) > 40: res+=1

# // If perfect score, print res and +
if res == players: print(f"{res}+")

# // Else just print res
else: print(res)