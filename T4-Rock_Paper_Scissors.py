import random
def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return "You won the game", 1, 0
    else:
        return "Computer won the game", 0, 1


def main():
    user_score = 0
    computer_score = 0
    choices = ['scissors', 'paper', 'rock']

    print("** Welcome to Rock-Paper-Scissors Game **")

    while True:
        print("\nCurrent Scores:")
        print(f"You: {user_score} | Computer: {computer_score}")

        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)

        print("\nYou chose:", user_choice)
        print("Computer chose:", computer_choice)

        result, user_point, computer_point = winner(user_choice, computer_choice)
        print(result)

        user_score += user_point
        computer_score += computer_point

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nFinal Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing the game...")
            break


game=main()