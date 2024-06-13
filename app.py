# write 'hello world' to the console
print('Welcome to the Rock, Paper, Scissors game!')

# import the random module for generating random choices
import random

def play_game():
    score = 0
    rounds = 0
    choices = ['rock', 'paper', 'scissors']

    while True:
        # prompt the player to enter their choice
        player_choice = input("Enter your choice (rock, paper, or scissors): ")
        # check if the player's choice is valid
        if player_choice not in choices:
            # if not, inform the player and continue with the next iteration
            print("Invalid choice. Please try again.")
            continue

       # generate a random choice for the opponent
        opponent_choice = random.choice(choices)
        rounds += 1

        # check the result of the round
        if player_choice == opponent_choice:
            # if the player's choice is the same as the opponent's, it's a tie
            print("It's a tie!")
        elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
             (player_choice == 'paper' and opponent_choice == 'rock') or \
             (player_choice == 'scissors' and opponent_choice == 'paper'):
            print("You won!")
            # increment the player's score
            score += 1
        else:
            # otherwise, the player loses
            print("You lost!")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print(f"You won {score} out of {rounds} rounds.")

play_game()