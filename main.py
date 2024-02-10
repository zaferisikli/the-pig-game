import random
def roll():
     min_val= 1
     max_val= 6
     roll = random.randint(min_val , max_val)

     return roll

while True:
    players= input("ENTER THE NUMBER OF PLAYERS(2-4):")
    if players.isdigit():
        players= int(players)
        if 2 <= players <= 4:
            break
        else:
            print("MUST BE BETWEEN 2 - 4 PLAYERS.")

    else:
        print("INVALID")

max_scores = 50
player_scores = [0 for _ in range(players)]
while max(player_scores) < max_scores:

    for player_index in range(players):
        print("\n player number " , player_index + 1 , "turn has just started!\n")

        current_score = 0
        while True:

           should_roll= input("WOULD YOU LIKE  TO ROLL (y)?")
           if should_roll.lower() != "y":
              break

           value = roll()
           if value == 1:
              print("you rolled 1 turn done")
              current_score = 0
              break
           else:
                current_score += value
                print("you rolled a:" ,value)


           print("YOUR SCORE İS:", value)
           player_scores[player_index] += current_score
           print("YOUR TOTAL SCORE İS:" , player_scores[player_index])