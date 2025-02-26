import os
s=input("Enter your name User 1: ")
q=input("Enter your name User 2: ")
def printBoard(gameValues):
    # Printing Board By using gameValues 's List
    print(f" {gameValues[0]} | {gameValues[1]} | {gameValues[2]} ")
    print(f"---|---|---")
    print(f" {gameValues[3]} | {gameValues[4]} | {gameValues[5]} ")
    print(f"---|---|---")
    print(f" {gameValues[6]} | {gameValues[7]} | {gameValues[8]} ")

def checkWin(gameValues):
    # All Winning Patterns
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        # if gameValues matches with the pattern and has X then X won the Match
        if(gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'X'):
            printBoard(gameValues)
            print(s,"Won the match")
            print("Better luck next time",q)
            return 1

        # if gameValues matches with the pattern and has X then O won the Match
        if(gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'O'):
            printBoard(gameValues)
            print(q,"Won the match")
            print("Better luck next time",s)
            return 0

        # if all places are filled and no one is the winner
        if all(isinstance(item, str) for item in gameValues):
            printBoard(gameValues)
            return -2
    # return -1 if no one wins
    return -1

if __name__ == '__main__':
    print("Welcome to the Game",s,"and",q)
    print("Good luck!")
    gameValues=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    chance = 1

    while(True):
        try:
            if chance == 1:
                printBoard(gameValues)
                print(s,"It's your Chance")
                value = int(input("\nPlease enter a value: "))

                # check if already filled with O
                if gameValues[value]!= 'O':
                    gameValues[value] = 'X'
                else:
                   
                    print("\nPlease Enter Different Location for X")
                    continue
                

            if chance == 0:
                printBoard(gameValues)
                print(q,"It's your Chance")
                value = int(input("\nPlease enter a value: "))

                # check if already filled with X
                if gameValues[value]!= 'X':
                    gameValues[value] = 'O'
                else:
                   
                    print("\nPlease Enter Different Location for O")
                    continue
               

        except IndexError:
            # exception if Value is not between 0 to 8 
            
            print("\nOops!! Please Enter value from 0 - 8\n")
            continue

        # for giving chance to other player
        chance = 1 - chance
        cwin = checkWin(gameValues)
        # Game Draw
        if(cwin == -2):
            print("Phew!It's a draw.\nWhat a match. Looks like you both are geniuse!!.")
            break
        # Match Over
        if(cwin != -1):
            print("Congratulations on your win!!")
            break
