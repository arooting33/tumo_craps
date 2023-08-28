# if sum of rolled dice is 7 or 11 player wins
# if sum is 2, 3 or 12 the casino wins
# if during first roll the sum is 4,5,6,8,9 or 10 that number becomes the goal number
# to win the player should roll the dice till they roll the goal number, if player rolls 7 before rolling the goal they lose

import random

def rolldice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1, dice2

def display_sum(dice1, dice2):
    print(f"the sum of dice 1 and dice 2 is {dice1} + {dice2} = {dice1 + dice2}")

def winner():
    print("You are a winner")

def loser():
    print("you are a loser, try again")

def gameover():
    print("game over")

def main(): 
    dice1, dice2 = rolldice()
    sum = dice1 + dice2
    display_sum(dice1, dice2)
    if sum in (7, 11):
        winner()
    elif sum in (2, 3, 12):
        loser()
    else: 
        goal = sum 
        print("now your goal is " + str(sum))
        while True: 
            dice3, dice4 = rolldice()
            sum3 = dice3 + dice4
            display_sum(dice3, dice4)

            if sum3 == goal: 
                winner()
                break
            if sum3 == 7:
                loser()
                break
        gameover()

         
    
if __name__ == "__main__":
    main()