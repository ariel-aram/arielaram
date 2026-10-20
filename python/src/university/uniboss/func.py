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
        with open(filename, 'rt', encoding='utf-8') as a:
            return [line.strip() for line in a if line.strip()]
    except:
        print("There was an error when opening the file.")
        return []

def insert_score(filename, game):
    try:
        a = open(filename, 'a')
    except:
        print("There was a fucking error when opening the fucking file.")
    else:
        a.write(f"{game}\n")
    finally:
        a.close()

def read_file(filename):
    try:
        a = open(filename, 'rt')
    except:
        print("There was a fucking error when opening the fucking file.")
    else:
        print(a.read())
    finally:
        a.close()

def openReadFile(filename):
    return open(filename, "rt", encoding="utf-8")
