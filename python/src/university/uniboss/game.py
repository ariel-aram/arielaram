from pathlib import Path
import func as fh
import draw as d
from random import choice

CURRENT_DIR = Path(__file__).resolve().parent

def play():
    list_words = list()
    archive = fh.openReadFile(CURRENT_DIR / "words.txt")
    for line in archive:
        word = line.strip()
        list_words.append(word)

    word_chosen = choice(list_words)

    for x in range(50):
        print()

    list_inputs = []
    corrected = []
    errors = 0

    name = input("Who's this? ")

    while True:
        guess = d.display_secret_word(word_chosen, corrected)

        # CONDITION FOR GUESSES
        if guess == word_chosen:
            print("You did it!")
            break

        # TRIES
        tries = input("\nInput a word: ").lower().strip()
        if tries in list_inputs:
            print("You already typed this shit...")
            continue
        else:
            list_inputs += tries # Or append
            if tries in word_chosen:
                corrected += tries
            else:
                print("Wrong letter.")
                errors += 1

        score = d.draw_forca(errors)

        # CONDITION FOR END OF THE GAME
        if errors == 6:
            print(f"You lost! The word was {word_chosen}")
            break

    if score > 0:
        fh.insert_score(CURRENT_DIR / "scores.txt", f"Player: {name} | Score: {score} | Word: {word_chosen}")
