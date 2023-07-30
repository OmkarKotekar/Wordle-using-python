# Wordle Game

This repository contains a simple Python implementation of the Wordle game. Wordle is a word puzzle game where the player needs to guess a randomly selected 5-letter word.

## How to Play

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/wordle-game.git
```

2. Make sure you have Python installed on your system.

3. Run the `wordle.py` script:

```bash
python wordle.py
```

4. The game will randomly select a 5-letter word from the predefined word list.

5. You have six attempts to guess the word correctly.

6. Each time you guess a letter, the game will provide feedback:

   - If you guess a letter that exists in the word and it is in the correct position, it will be marked with a '*'.
   - If you guess a letter that exists in the word but it is in the wrong position, it will be marked with a '!'.
   - If the letter does not exist in the word, it will be marked with a '-'.

7. Continue guessing until you either guess the entire word correctly or run out of attempts.

## Word List

The game uses a predefined list of words from which it selects the secret word. The current word list includes:

```
apple, chair, beach, baker, table, watch, music, house, juice, party
```

You can modify this list in the `word_list` variable within the `wordle.py` script.

## Requirements

The game script uses the `random` module, which is part of the Python standard library. No additional dependencies are required.

Have fun playing Wordle! If you encounter any issues or have suggestions for improvement, feel free to open an issue or contribute to the repository. Happy word guessing!