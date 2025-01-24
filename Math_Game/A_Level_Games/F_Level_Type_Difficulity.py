# Difficulty function

def showDifficulty(level):
    if level >= 200:
        print("-----Difficulty : Impossible--------")
    elif level >= 100:
        print("-----Difficulty : Ballistic--------")
    elif level >= 75:
        print("-----Difficulty : Raging--------")
    elif level >= 50:
        print("-----Difficulty : Challenging--------")
    elif level >= 40:
        print("-----Difficulty : Expert--------")
    elif level >= 30:
        print("-----Difficulty : Advanced--------")
    elif level >= 20:
        print("-----Difficulty : Hard--------")
    elif level >= 10:
        print("-----Difficulty : Medium--------")
    else:
        print("-----Difficulty : Easy--------")