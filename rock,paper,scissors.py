import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    print("Welcome to Rock, Paper, Scissors — Best of 5!")

    while rounds < 5:
        user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid input. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "user":
            print("✅ You win this round!")
            user_score += 1
        elif winner == "computer":
            print("💻 Computer wins this round!")
            computer_score += 1
        else:
            print("🤝 It's a tie. No points.")

        rounds += 1
        print(f"Score -> You: {user_score} | Computer: {computer_score}")

    print("\n🏁 Final Result:")
    if user_score > computer_score:
        print("🎉 Congratulations! You won the best of 5 series!")
    elif computer_score > user_score:
        print("😞 Computer wins the best of 5 series. Better luck next time!")
    else:
        print("🤝 It's a tie overall!")

if __name__ == "__main__":
    play_game()
