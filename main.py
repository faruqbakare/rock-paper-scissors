import random
while True:
    user_choice = input('please enter your choice (rock, paper or scissors): ')
    possible_choices = ['rock', 'paper', 'scissors' ]
    while user_choice not in possible_choices:
        user_choice = input("please enter valid input")
    cpu_actions = random.choice(possible_choices)
    print(f'you chose {user_choice} and the cpu chose {cpu_actions}')
    while user_choice not in possible_choices:
        user_choice = input("please enter valid input")
    if user_choice == cpu_actions:
        print(f'both users selected {user_choice}, its a tie!')
    elif user_choice == 'rock':
        if cpu_actions == 'scissors':
            print(f'rock smashes scissors, you win!')
        else:
            print(f'paper covers rock, cpu wins!')
    elif user_choice == "paper":
        if cpu_actions == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if cpu_actions == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break