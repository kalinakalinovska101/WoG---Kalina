def welcome_user():
    # Prompt the user for their name
    global name
    print("""
==========================================================
----------------------------------------------------------
Welcome to World of Gaming!
----------------------------------------------------------
==========================================================""")
    name = input("""
    Please enter your name: """).strip()
    if not name:
        print("""You need to enter your name!
              """)
        return welcome_user()
    # Create a welcoming message
    welcome_message = f"""
==========================================================
----------------------------------------------------------
Hello, {name} and welcome to the World of Games (WoG)."
Here you can find many cool games to play.
You have total of 3 attempts!
----------------------------------------------------------
=========================================================="""

    # Print the welcome message
    print(welcome_message)

#welcome_user()

# Choosing a game to play
def load_game():
    print("""
==========================================================
Please choose a game to play:
----------------------------------------------------------
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
==========================================================
""")
    global game
    choice = input("""
    Enter your choice (1, 2 or 3): """).strip().lower()

    if choice == '1':
        print("You choose the Memory Game.")
        game = 1
    elif choice == '2':
        print("You choose the Guess Game.")
        game = 2
    elif choice == '3':
        game = 3
        print("You choose the Currency Roulette Game.")
    else:
        print("Invalid choice. Please select 1, 2 or 3.")
        return load_game()
#load_game()

# Choosing difficulty for the game
def load_difficulty():
    print("""
==========================================================
Please choose game difficulty from 1 to 5:
==========================================================
    """)

    choice = input("""
    Enter your difficulty (from 1 to 5): """).strip().lower()

    global difficulty
    if choice == '1':
        difficulty = 1
        print("You choose difficulty 1.")
    elif choice == '2':
        difficulty = 2
        print("You choose difficulty 2.")
    elif choice == '3':
        difficulty = 3
        print("You choose difficulty 3.")
    elif choice == '4':
        difficulty = 4
        print("You choose difficulty 4.")
    elif choice == '5':
        difficulty = 5
        print("You choose difficulty 5.")
    else:
        print("Invalid choice. Please select 1 to 5!")
        return load_difficulty()
#load_difficulty()



