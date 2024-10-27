import random
def game():
    options=["rock","paper","scissors"]
    while True:
        print("Game Instructions:\n 1.The user wins:\n a.user choice = rock and computer choice = scissors \n b.user choice = paper and computer choice = rock\n")
        print("c.user choice = scissors and computer choice = paper\n 2.The user loses\n 3. Its a tie if user choice = computer choice")
        user_choice=input("enter rock,paper,scissors or quit:").lower()
        computer_choice=random.choice(options)
        print("Computer choice:",computer_choice)
        if (user_choice == "quit"):
            print("Thanks for playing!")
            break
        elif(user_choice not in options):
            print("Invalid choice.Please try again.")
            continue
        elif(user_choice == computer_choice):
            print("Its a tie!")
        elif(user_choice == "rock" and computer_choice == "scissors"):
            print("You win!")
        elif(user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        elif(user_choice == "scissors" and computer_choice =="paper"):
            print("You win!")
        else:
            print("You lose!")
game()
        
