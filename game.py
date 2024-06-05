import random

def get_user_choice():
    """Get the user's choice"""
    user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
    while user_choice not in ['rock', 'paper', 'scissor']:
        print("Invalid choice. Please choose either 'rock', 'paper', or 'scissor'.")
        user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
    return user_choice

def get_computer_choice():
    """Randomly select the computer's choice"""
    choices = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    """Determine the winner between user and computer"""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if ((user_choice == 'rock' and computer_choice == 'scissor') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissor' and computer_choice == 'paper')):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play a single round of the game"""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer's choice: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

def main():
    """Main function to run the game"""
    print("Welcome to Rock, Paper, Scissor Game!")
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
