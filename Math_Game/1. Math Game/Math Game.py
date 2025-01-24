# Importing the level mode
from Math_Game.A_Level_Games.A_Level_Type_Mode import *

# Importing the quick maths mode
from Math_Game.B_Quick_Maths.A_Quick_Math_Mode import *

# Importing the beat the clock mode
from Math_Game.C_Beat_The_Clock.A_Beat_The_Clock_Mode import *

# Importing the practice mode
from Math_Game.D_Practice.A_Practice_Mode import *


# Data
level_type = ["1", "Level Type", "level type", "l", "L"]
quickMath = ["2", "Quick Math", "quick math", "Q", "q"]
beatTheClock = ["3", "Beat The Clock", "beat the clock", "b", "B"]
practice = ["4", "Practice", "practice", "p", "P"]

# Choosing the gamemode

# 1. Level Type
# 2. Quick Maths
# 3. Beat The Clock
# 4. Practice
# 5. Fight Againts Robot

print("\n----Welcome to this cool maths game----")


print("Choose your game mode : ")
print("\n1. Level Type")
print("2. Quick Maths")
print("3. Beat The Clock ")
print("4. Practice")

# Receive the user's choice on the gamemode

userChoice = input("\nWhich mode do you want (In Number Form) : ")

# Level Mode
if userChoice in level_type:
    Level_Mode()
elif userChoice in quickMath:
    quick_math()
elif userChoice in beatTheClock:
    beat_the_clock()
elif userChoice in practice:
    practiceMode()
else:
    print("\nInvalid choice.")



