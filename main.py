import random

CHOICES = {
    "1": "rock",
    "2": "scissors",
    "3": "paper",
}

# Each key beats its value
WINS_AGAINST = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}


def get_player_choice():
    """Ask the player for a move. Return None if they want to quit."""
    while True:
        print("\nChoose: 1 - rock, 2 - scissors, 3 - paper, q - quit")
        answer = input("> ").strip().lower()
        if answer == "q":
            return None
        if answer in CHOICES:
            return CHOICES[answer]
        print("Invalid input, please try again.")


def get_winner(player, computer):
    """Return 'draw', 'player' or 'computer'."""
    if player == computer:
        return "draw"
    if WINS_AGAINST[player] == computer:
        return "player"
    return "computer"


def main():
    player_score = 0
    computer_score = 0

    print("Rock Paper Scissors")

    while True:
        player = get_player_choice()
        if player is None:
            break

        computer = random.choice(list(CHOICES.values()))
        print(f"Computer chose: {computer}")

        result = get_winner(player, computer)
        if result == "player":
            player_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round.")
        else:
            print("It's a draw.")

        print(f"Score: you {player_score} : {computer_score} computer")

    print(f"\nFinal score: you {player_score} : {computer_score} computer")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()