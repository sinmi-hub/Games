# Hangman Game

This is a simple Hangman game implemented in Python. The game allows players to guess letters in order to uncover a hidden word. Players have a limited number of lives and can also request hints to help them guess the word. The difficulty of this version of hangman might be rated as hard, due to the fact that there is only 6 lives and three hints for user to successfuly win.

## How to Play

1. Run the `game.py` file to start the game.
2. The game will randomly select a word from a dictionary file based on the Unix OS.
3. Guess letters by entering them as input.
4. If the guessed letter is in the word, it will be revealed in the correct position.
5. If the guessed letter is not in the word, a life will be lost.
6. Players can also request hints to get additional information about the word.
7. The game continues until the player either guesses the word correctly or runs out of lives.

## Dependencies

This Hangman game relies on the following dependencies:

- Python 3.x
- Requests library for accessing the Merriam-Webster API
- Config file which contains personal API key

## API Integration

The game integrates with the Merriam-Webster API to provide word definitions and synonyms as hints. The API is used to enhance the gameplay experience by providing additional information about the hidden word. My personal API key is in a separate file called config. In order for the code to work properly, 2 API keys will be needed. One for Merriam Webster's Thesauraus and Merriam Webster's dictionary. These are represented in game.py as MW_API_DICTIONARY and MW_API_THESAURAUS, which are imported from config. **Due to security reasons, I will not be uploading config here.** Here is a link to get free API keys from Merriam Webster. *Feel free to simply replace the field mentioned above with your new API key, and its all good to go*. [Merriam Webster Free API](https://dictionaryapi.com/products/index)

## File Structure

- `game.py`: Contains the main game logic and user interface.
- `dictionary.txt`: A file containing a list of words used for word selection. This dictionary file is an exact copy of the Unix dictonary (dictionary used by unix systems). However, words less than 4 letters are filtered out to make the game a bit harder.

## How to Contribute

Contributions to this Hangman game are welcome! If you have any suggestions, bug fixes, or additional features to add, please feel free to submit a pull request.

## Acknowledgments

- The ASCII art used in the game is courtesy of [asciiart.co.uk](https://asciiart.website/).
- Some of the ascii art used in art.py is courtesy of [Angela Yu](https://www.udemy.com/course/100-days-of-code/?utm_source=adwords&utm_medium=udemyads&utm_campaign=Python_Search_la.EN_cc.US_PP_Control&utm_content=deal4584&utm_term=_._ag_141124569012_._ad_594266299590_._kw__._de_c_._dm__._pl__._ti_dsa-1652644802545_._li_9060031_._pd__._&matchtype=&gad_source=1&gclid=Cj0KCQiAh8OtBhCQARIsAIkWb6_qzTWgt9uj3DAq6XE5JNDuFFUwojBLIlOn81lvTS1QMdIOHmAoGTAaAr0yEALw_wcB)
- This game was inspired by the classic Hangman game.

