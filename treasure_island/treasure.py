# treasure.py
def choose_first_path(choice: str) -> str:
    choice = choice.strip().lower()
    return "lake" if choice == "left" else "hole"

def choose_second_path(choice: str) -> str:
    choice = choice.strip().lower()
    return "house" if choice == "wait" else "trout"

def choose_door(choice: str) -> str:
    choice = choice.strip().lower()
    if choice == "red":
        return "fire"
    elif choice == "blue":
        return "beasts"
    elif choice == "yellow":
        return "treasure"
    else:
        return "invalid"


def main():
    print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    choice1 = input("You're at a cross road, type 'left' or 'right':\n")
    path1 = choose_first_path(choice1)

    if path1 == "lake":
        choice2 = input("You've come to a lake. Type 'wait' for a boat or 'swim' to cross:\n")
        path2 = choose_second_path(choice2)
        if path2 == "house":
            choice3 = input("You arrive at a house with 3 doors: red, yellow, blue. Which color?\n")
            result = choose_door(choice3)
            if result == "treasure":
                print("You found the treasure! You Win!")
            elif result == "fire":
                print("It's a room full of fire. Game Over.")
            elif result == "beasts":
                print("You enter a room of beasts. Game Over.")
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You get attacked by an angry trout. Game Over.")
    else:
        print("You fell into a hole. Game Over.")


if __name__ == "__main__":
    main()
