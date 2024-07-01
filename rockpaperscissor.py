import random

user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")


    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")