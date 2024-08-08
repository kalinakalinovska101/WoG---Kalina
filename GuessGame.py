def guess_game():
#    The following is used only for test purposes!
#    name = 'Kalina'
#    difficulty = int(1)
    from Live import name, game, difficulty
    welcome_message = f"""
==========================================================
Hello, {name} and welcome to the Guess Game!"
The purpos of the Guess Game is to guess the number that 
the computer has chosen!
=========================================================="""
    print(welcome_message)
    print(f"Please, choose a number between 1 and {difficulty}")
    import random
    number = int(random.randint(1, difficulty))
#    The following is used only for test purposes!
    while True:
        try:
            guess = int(input("Enter the number to guess: "))
        except ValueError:
            print(f"Not a number. Please, enter a number between 1 and {difficulty}!")
            continue
        else:
            print("Yes, it is a number! We can play!")
            break
    if guess < number:
        print("""
        Unfortionately the number is too low! You did't get any points!
        """)
    elif guess > number:
        print("""
        Unfortionatelly the number is too high. You did't get any points!
        """)
    elif guess == number:
        print("""
        You are correct!
        """)
        from Score import add_score, current_score
        add_score()
        global current_score
        this_round_score = (difficulty * 3) + 5
        print(f"Your score from this round is: {this_round_score}")
        from Live import difficulty
        this_round_score = (difficulty * 3) + 5
        print(f"Your score from this round is: {this_round_score}")



