import random

print("🎮 Welcome to Rock, Paper, Scissors!")

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
    if user_choice not in choices:
        print("⚠️ Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"💻 Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win!")
    else:
        print("😢 You lose!")

    # Ask if user wants to play again
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing!")
        break