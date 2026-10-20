def display_secret_word(word, corrected):
    guess = ""
    for letter in word:
        if letter in corrected:
            guess += letter
        else:
            guess += "\u2588"
    print(f"GUESS ({len(word)}) letters: ")
    for letter in guess:
        print(letter, end=' ')
    print()

    return guess

def draw_forca(mistakes):
    score = 1000

    print("X==:==")
    print("X  :  ")
    if mistakes >= 1:
        print("X  O  ")
    else:
        print("X     ")

    if mistakes == 2:
        print("X  |  ")
    elif mistakes == 3:
        print("X /|  ")
    elif mistakes >= 4:
        print("X /|\\ ")
    else:
        print("X     ")

    if mistakes == 5:
        print("X /   ")
    elif mistakes >= 6:
        print("X / \\ ")
    else:
        print("X     ")

    print("X\n=======")

    score -= mistakes * 100
    print(f"Mistakes: {mistakes}/6 | Current score: {max(0, score)}")
    return max(0, score)
