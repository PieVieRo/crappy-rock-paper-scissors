from random import choice
import time


def game():
    """
    Here we define the game
    """
    # getting the input from the player
    # and randomizing the computer choice
    player = ''
    moves = ["rock", "paper", "scissors"]

    while player not in moves:
        player = input("Your choice: ").lower()
        if player not in moves:
            print("you didn't choose the correct option")
    computer = choice(moves)
    print("Computer chose", computer)

    time.sleep(1.5)
    print('\n')
    print("it is {} vs {}!".format(player, computer))

    time.sleep(1.5)
    # check if it's a draw
    if player == computer:
        print("It's a draw!")

    # check who won
    elif player == "paper":
        if computer == "scissors":
            print("Computer won!")
        else:
            print("You won!")

    elif player == "scissors":
        if computer == "rock":
            print("Computer won!")
        else:
            print("You won!")

    elif player == "rock":
        if computer == "paper":
            print("Computer won!")
        else:
            print("You won!")

    time.sleep(1)
    # asking the player if they want to play again
    print("Do you want to play again? [y/n] ")
    again = input().lower()
    if again == 'y' or again == 'yes':
        game()
    else:
        print("goodbye")


if __name__ == '__main__':
    game()
