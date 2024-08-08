def currency_roulette_game_wellcome():
#   Prerequisite is currency_converter
#    The following is used only for test purposes!
#    name = 'Kalina'
#    difficulty = int(1)
    global name
    from Live import name, game, difficulty
    welcome_message = f"""
==========================================================
Hello, {name} and welcome to the Currency Roulette Game!"
The purpos of the Currency Roulette Game is to try and 
guess the value of a random amount of USD in ILS!
=========================================================="""
    print(welcome_message)


def get_guess_from_user():
    get_money_interval()
    def check_imput():
        global guess
        while True:
            global amount_of_ILS
            try:
                guess = int(input(f"Enter the amound of USD that are in {amount_of_ILS} amount of ILS:"))
            except ValueError:
                print(f"Not a number. Please, enter a positive number! (not 0)")
                continue
            else:
                print("Yes, it is a correct entry!")
                exit
            break
    check_imput()


def get_money_interval():
    global amount_of_ILS
    global low_range
    global high_range
    global number
    import random
    global current_currency_rate
    from Live import difficulty
    number = int(random.randint(5, 105))
    low_range = (number - (5 - difficulty))
#    print(low_range)
    high_range = (number + (5 - difficulty))
#    print(high_range)
    from currency_converter import CurrencyConverter
    c = CurrencyConverter()
    c.convert(1, 'USD', 'ILS')
#    print(c.convert(1, 'USD', 'ILS'))
    actual_price = c.convert(1, 'USD', 'ILS')
    amount_of_ILS = number * actual_price
    amount_of_ILS = format(amount_of_ILS, ".2f")
#    print(number)

def compare():
    if low_range < guess < high_range:
        print("""
        You are correct!
        """)
        from Score import add_score, current_score
        add_score()
        global current_score
        from Live import difficulty
 #       global difficulty
        this_round_score = (difficulty * 3) + 5
        print(f"Your score from this round is: {this_round_score}")
    else:
        print("""
        Unfortionately the number is too low or too high! You did't get any points!
        """)


def play():
    amount_of_ILS = 0
    hight_range = 0
    low_range = 0
    currency_roulette_game_wellcome()
    get_guess_from_user()
    compare()


