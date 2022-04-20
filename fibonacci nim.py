# Fibonacci Nim game
# each player pick number of coins which is from 1 to at most twice the previous move
# the number of coins that picked by the players must be removed from all coins and the player who pick the last coin be the winner
# Author: Ahmed Reda Elsayed
# Date: 27-02-2022


def coins_input():  # input the number of coins to start play
    global player2, coins
    coins = int(input("number of coins: "))

    # good operation to connect between the main range during play and range of the first pick
    player2 = (coins - 1) / 2


def player1_input():  # player1 pick from coins
    global player1, player2, coins
    player1 = int(input(f"range from 1 to {player2 * 2}\nplayer1: "))
    print("**************************")
    while player1 < 0 or player1 > player2 * 2 or player1 > coins:  # defense as if player choose wrong
        player1 = int(input(
            f"wrong input\ncoins is: {coins}\nrange from 1 to {player2 * 2}\nplayer1: "))
        print("**************************")
    coins -= player1  # decrese all coins by number of coins that picked by player1


def player2_input():  # player2 pick from coins
    global player1, player2, coins
    player2 = int(input(f"range from 1 to {player1 * 2}\nplayer2: "))
    print("**************************")
    while player2 < 0 or player2 > player1 * 2 or player2 > coins:  # defense as if player choose wrong
        player2 = int(input(
            f"wrong input\ncoins is: {coins}\nrange from 1 to {player1 * 2}\nplayer2: "))
        print("**************************")
    coins -= player2  # decrese all coins by number of coins that picked by player2


def game():  # main game function

    global player1, player2, coins

    coins_input()

    while coins > 0:
        player1_input()
        if coins == 0:  # check if player1 win
            print("player1 win")
            break
        print(f"coins is: {coins}")

        player2_input()
        if coins == 0:  # check if player2 win
            print("player2 win")
            break
        print(f"coins is: {coins}")


game()
