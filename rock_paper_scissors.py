import random


print('Welcome in my Rock-Paper-Scissors game!')
input('Enter to continue ')


def start_game():

    # while user_input != paper or user_input != rock or user_input != scissors loop will start again and again
    while True:
        print('\n')
        user_input = input(
            'Choose your option:\nrock,\nscissors,\npaper\n ==> ')
        if (user_input.lower() == 'rock') or (user_input.lower() == 'scissors') or (user_input.lower() == 'paper'):
            break
    computer = computer_choice()
    print('Computer: ', computer)
    winner(user_input, computer)
    next_round()


def computer_choice():
    """Generate pseudorandom number and return 'paper' or 'rock' or 'scissors'"""
    random_number = random.randint(0, 2)
    computer_option = {
        0: 'paper',
        1: 'rock',
        2: 'scissors'
    }
    return computer_option[random_number]


def winner(user, computer):
    """compares the values ​​of variables and print who won"""
    if user == computer:
        print("It's tie!")

    elif user == 'rock':
        if computer == 'paper':
            print('Computer won!')
        if computer == 'scissors':
            print('User won!')

    elif user == 'paper':
        if computer == 'scissors':
            print('Computer won!')
        if computer == 'rock':
            print('User won!')

    elif user == 'scissors':
        if computer == 'rock':
            print('Computer won!')
        if computer == 'paper':
            print('User won!')


def next_round():
    """asks user about next round """
    print('\n----------------')
    next_round = input('Do you want play next round?\n yes \n no\n ==> ')
    if next_round.lower() == 'yes':
        start_game()
    print('----------------\n')


start_game()


input('Enter anything to exit')
