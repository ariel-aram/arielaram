help(print)
print("Hello fucking world", end=' ')
print("I'm blind so I just yell this shit")

def addition(x = 0, y = 0, z = 0):
    '''
    This function adds three numbers together.
    :param x: The first number.
    :param y: The second number.
    :param z: The third number.
    :return: The sum of x, y, and z.
    '''
    return x + y + z

print(addition(1,2,3))
help(addition)

def valid_int(question, min, max):
    x = int(input(question))
    while((x < min) or (x > max)):
        x = int(input(question))
    return x

def factorial (num):
    '''
    This function calculates the factorial of a number.
    :param num: The number to calculate the factorial of.
    :return: The factorial of num.
    '''
    fat = 1
    if num == 0:
        return fat
    # This shit only executes in case num > 0
    for i in range(1, num + 1, 1):
        fat *= i
    return fat

try:
    x = valid_int("Input a value to calculate the fatty: ", 0, 999999)
    print(f"{x}! = {factorial(x)}")
except ValueError:
    print("Invalid input. Please enter an integer.")

help(factorial)

def existsFile(filename):
    try:
        a = open(filename, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createFile(filename):
    try:
        a = open(filename, 'wt+')
        a.close()
    except:
        print("There was a fucking error when creating the fucking file.")
    else:
        print(f"File {filename} has been created successfully.\n")

def registerGame(filename, gameName, videogameName):
    try:
        a = open(filename, 'at')
    except:
        print("There was a fucking error when opening the fucking file.")
    else:
        a.write(f"Game: {gameName}; Videogame: {videogameName}\n")
    finally:
        a.close()

def listFile(filename):
    try:
        a = open(filename, 'rt')
    except:
        print("There was a fucking error when opening the fucking file.")
    else:
       print(a.read())
    finally:
        a.close()

# Main Programme
file = 'dream_items.txt'
if existsFile(file):
    print("File found...")
else:
    print("File not found...I'm creating it now")
    createFile(file)

while True:
    print("FEVER MENU")
    print("1 - Register a dream item.")
    print("2 - List registrations.")
    print("3 - Pull the middle finger.")

    op = valid_int("Choose an option: ", 1, 3)
    if (op == 1): # New item
        print("New item option selected...\n")
        gameName = input("Type the game name: ")
        videogameName = input("Type the videogame name: ")
        registerGame(file, gameName, videogameName)
    elif (op == 2): # List items
        print("Listing option selected...\n")
        listFile(file)
    elif (op == 3):
        print("Fuck off asshole...leaving...")
        break
