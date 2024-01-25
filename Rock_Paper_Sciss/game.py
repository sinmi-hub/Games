from time import sleep
from random import choice

valid_choice = ['s', 'r', 'p', 'q']
outcomes = {'r': {'s': 'win', 'p': 'lose'}, 'p': {'r': 'win', 's': 'lose'}, 's': {'p': 'win', 'r': 'lose'}}

def print_welcome_message():
    print('''
                    _    
                   | |   
    _ __ ___   ___ | | __ 
    | '__/ _ \ / __| |/ /  
    | | | (_) | (__|   < 
    |_|  \___/ \___|_|\_\\ _ __ _
    | '_ \ / _` | '_ \ / _ \ '__|
    | |_) | (_| | |_) |  __/ |   
    | .__/ \__,_| .__/ \___|_|   
    | |         | |              
    |_|_   __ _ |_|  __  ___  _ _ _ __                         
    / __|/ __| / __/ __|/ _ \| '__/ __|
    \__ \ (__| \__ \__ \ (_) | |  \__ \\
    |___/\___|_|___/___/\___/|_|  |___/
                                            
''')
    print('\n'+'Welcome to Rock, Paper, Scissors v 1.5.1...!')
    sleep(0.8)

def get_player_choice():
    while True:
        print('''
Rock -- Enter 'r' for Rock
Paper -- Enter 'p' for Paper
Scissors -- Enter 's' for Scissors
Enter 'q' to quit
        ''')
        p1_choice = input('Enter your choice: ').lower() # get player 1 choice

        if p1_choice in valid_choice:
            return p1_choice
        else:
            print('Invalid choice. Please try again.')

def print_result(p1_choice, p2_choice):
    result = outcomes[p1_choice].get(p2_choice)
    print(f'You chose {p1_choice} and the bot chose {p2_choice}.')
    print(f'You {result}!') if result is not None else print("It's a tie!")

def play_again():
    while True:
        play_again = input('Play again? (y/n): ').lower()
        if play_again == 'n':
            print('Thanks for playing!')
            print('Exiting...')
            sleep(0.4)
            return False
        elif play_again == 'y':
            return True
        else:
            print("Please enter 'y' or 'n'.")

def play_game():
    print_welcome_message()
    sleep(0.5)

    while True:
        p1_choice = get_player_choice()

        if p1_choice == 'q':
            print('Thanks for playing!')
            break

        p2_choice = choice(['r', 'p', 's']) # get player 2 choice. random generated
        print_result(p1_choice, p2_choice)

        sleep(0.3)
        print()

        if not play_again():
            break

play_game()
