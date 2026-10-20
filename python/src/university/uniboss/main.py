from pathlib import Path
import game as gg
import func as fh 

CURRENT_DIR = Path(__file__).resolve().parent 

def show_menu():
    print("=" * 30)
    print("UNIBOSS MAIN MENU")
    print("=" * 30)
    print("1 - PLAY.")
    print("2 - SCORE.")
    print("3 - EXIT.")
    print("=" * 30)

archive = CURRENT_DIR / "scores.txt"

if fh.existsFile(archive):
    print("File found...")
else:
    print("File not found...I'm creating it now")
    fh.createFile(archive)

while True:
    show_menu()
    option = int(input("Choose an option (1-3): "))

    if option == 1:
        print("Start gaem...")
        gg.play()
    elif option == 2:
        print("SCORES")
        data = fh.listFile(archive)
        if not data:
            print("No scores yet...")
        else:
            for i, score_entry in enumerate(data, start=1):
                print(f"{i} -> {score_entry}")
                
    elif option == 3:
        print("Thanks for playing!")
        break
    else:
        print("Invalid option. You're now holding explosives")
