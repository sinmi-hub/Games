from random import randint
from requests import get
from art import * # stages, logo
from time import sleep
from os import system
from config import *


words = []
lives = [('❤' *(i)) for i in range(len(stages))]
stage = 5
hints = 3

def loading_screen():
    print(logo)
    words = read_words()
    print("Welcome to Hangman v1.5.0..!")



# read words from the unix dictionary file (dict). We filter out words that are less than 4 characters long and words that contain an apostrophe to make the game more logical.
def read_words():  
    with open('Hangman/words.txt', 'r') as file:
        for line in file:
            if len(line) > 4 and ('\'' not in line):
                words.append(line.strip())

def pick_rand_word()->str:
    rand_index = randint(0, len(words)-1)
    return (words[rand_index]).lower()

def get_user_input():
    user_input = input("Guess a letter or enter \'hint\' to get a hint: ")
    
    while True:
        if len(user_input) > 1 and user_input.lower() != 'hint':
            user_input = input("Please enter a single letter: ")
        elif not user_input.isalpha():
            user_input = input("Please enter a letter: ")
        else:
            break
        
    return user_input

# checks to see if the user input is in the word and if it has been guessed before
def check_user_input(usr_inpt:str, word:str, guess:list): 
    state = usr_inpt in word and (word.count(usr_inpt) != guess.count(usr_inpt))

    if state:
        idx_pos = word.index(usr_inpt) # Exception won't be raised
        if guess[idx_pos] == '_':
            guess[idx_pos] = usr_inpt

        # finds next possible occurrence. Minimizes use of for loops
        else:
            for i in range(idx_pos + 1, len(word)):
                if word[i] == usr_inpt and guess[i] == '_':
                    guess[i] = usr_inpt
                    break           
    else:
        wrong_guess()

# displays the hangman stage and informs the user that they have lost a life
def wrong_guess():
    global stage
    print("Wrong guess!", "You have lost a life.")
    print(stages[stage])
    stage -= 1
    sleep(1.8)

# returns the definition of the word using MERRIAM WEBSTER's API
def get_meaning(word:str)->str:
    url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={MW_API_DICTIONARY}'
    response = get(url)

    # check if the request was successful
    if response.status_code != 200:
        print("Error: ", response.status_code)
        return None
    
    data:list = response.json()

    # response using MERRIAM WEBSTER's API should be returned as a list that contains a single dictionary
    if (isinstance(data, list)):
        word_information:dict = data[0]
        
        # we look for the short definition of the word
        if isinstance(word_information, dict) and 'shortdef' in word_information.keys():
            definition = word_information['shortdef']
            definition = [defn[:defn.index(':')] if ':' in defn else defn
                          for defn in definition ]
            return ", ".join(definition)
        
        elif isinstance(word_information, str):
            return word_information
        
        else:
            return None
    else:
        return None    

# returns the synonyms of the word using MERRIAM WEBSTER's API. Steps are similar to get_meaning() but we look for the synonyms of the word. The structure of the API response is deeply nested so we have to be careful when accessing the data. API returns a list. i.e data. This list contains a single dictionary. i.e word_info. This dictionary different dictionaries as values, but we focus on the first dictionary. This has the key meta. i.e meta_field. This dictionary contains a list of synonyms. i.e syns. This list contains a single list of synonyms. i.e word_syns. We return the first 5 synonyms of the word.
def get_synonyms(word)->str:
    url = f'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={MW_API_THESAURUS}'
    response = get(url)

    if response.status_code != 200:
        print('Error', {response.status_code})
        return None
    
    data = response.json() # returns the API result

    if (isinstance(data, list)):
        word_info = data[0]

        if isinstance(word_info, dict) and 'meta' in word_info:
            meta_field = word_info['meta']
            if isinstance(meta_field, dict) and 'syns' in meta_field:
                syns = meta_field['syns']
                word_syns = syns[0]
                if len(word_syns) > 5:
                    return ", ".join(word_syns[:5])
                else:
                    return ", ".join(word_syns)
            else:
                return None
        else:
            return None
    
    else:
        return None
    
# returns the hints for the word
def get_hints(word)->list:
    defn = get_meaning(word)
    syn = get_synonyms(word)
    word_meanings = f'Meaning: {defn}' if defn is not None else 'No suitable meaning found.'
    word_synonyms = f'Synonyms: {syn}' if syn is not None else 'No suitable synonyms found.'
    word_length = f'Length: The word is {len(word)} letters long.'
    return [word_meanings, word_synonyms, word_length]


# initializes the game by picking a random word and creating a list of underscores that is the same length as the word
def init_game()->tuple:
    loading_screen()
    sleep(0.8)
    print("Loading...\n")
    word = pick_rand_word()
    guess = ['_' for i in range(len(word))]
    sleep(0.7)
    return word, guess

# displays how many lives the user has left and the current state of the word
def user_experience(guess:list, curr_hints:list):
    print(f'{lives[stage]}\t\t\t\tHints left:{hints}\n')

    if stage < 5:
        print("\t",(''.join(guess)).capitalize(), "\n", stages[stage], "\n")
    else:
        print("\t",''.join(guess).capitalize(), "\n")
    
    if len(curr_hints) > 0:
        print("Hints used: ")
        for hint in curr_hints:
            print(hint)
        print()

# displays the final message to the user
def final_msg(word, stage:int):
    print()
    if stage == 0:  
        print('GAME OVER!')
        print(f'The word was {word}.\nExiting...')
        
    else:
        print("Congratulations! You have won the game.")
        print(f'The word was {word}.\nExiting...')


def game_play():
    global hints
    word, guess = init_game()
    all_hints = get_hints(word)
    curr_hints = []
    game_over = False
    
    while not game_over:
        user_experience(guess, curr_hints)
        user_input = get_user_input()

        # check if the user wants a hint
        if user_input.lower() == 'hint' and hints > 0:
            rand_hint = all_hints.pop(randint(0, hints-1))
            hints -= 1
            print(rand_hint)
            curr_hints.append(rand_hint)
            sleep(2)
        
        elif user_input.lower() == 'hint' and hints == 0:
            print("You have no hints left.")
            
        # user is guessing a letter
        else:
            check_user_input(user_input, word, guess)

        system('clear')

        if stage == 5:
            loading_screen()

        # check if the user has won the game or ran out of lives
        if '_' not in guess or stage == 0:
            game_over = True 
        
    final_msg(word, stage)
    sleep(2)


game_play()

