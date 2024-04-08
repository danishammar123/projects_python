import random

options = ("rock", "paper", "scissors")
running = True
player_wins = 0
computer_wins = 0

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        player_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

    print(f"You: {player_wins}, Computer: {computer_wins}")

    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again in ('y', 'n'):
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    if play_again == "n":
        running = False

print("Thanks for playing!")


