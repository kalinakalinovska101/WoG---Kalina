# is numetic was not working
def compare_data():
    from Live import name, game, difficulty
    computer_list.sort()
    user_list.sort()
    print(f"""
The entered list is: {user_list}
The generated from the computer is: {computer_list}""")
    if computer_list == user_list:
        global result
        result = 0
        result = True
        from Score import add_score, current_score
        add_score()
        return True
    else:
        result = False
        print(f'Unfortionately this was wrong. No points were gained!')
        return False


def play_memory_game():
    from Live import name, game, difficulty
    welcome_message = f"""
==========================================================
Hello, {name} and welcome to the Memory Game!"
The purpos of the Memory Game is to remember the numbers 
generated by the computer!
=========================================================="""
    print(welcome_message)
    n = input('Press any key when you will ready to start.\nTo quit press "q". ')
    if n == 'q':
        print(f'You choose to quit game... No points will be gained.')
        return False

    def generate_sequence():
        import random
        from Live import name, game, difficulty
        global computer_list
        computer_list = random.sample(range(1, 101), difficulty)
    generate_sequence()

    print(f"""Look and remember: 
{computer_list}""")
    import time
    time.sleep(0.7)

    def clear_screen():
        import os, sys, subprocess
        operating_system = sys.platform
        if operating_system == "win32":
            subprocess.call('cls', shell=True)
        elif operating_system == "linux":
            subprocess.call('clear', shell=True)
    clear_screen()

    def get_data_from_user():
        global user_list
        user_list = input('Enter numbers separated by space, the numbers must be between 1 and 100: ')
        user_list = user_list.split()
        isintlist = [s for s in user_list if s.isdigit()]
        if isintlist == []:
            print("You have entered an invalid input. Please, enter ONLY numbers separated by space.")
 #           get_data_from_user()
        else:
            user_list = [eval(i) for i in user_list]
            print("Your answer is: ", user_list)
        def check_data_from_user():
            from Live import difficulty
            global user_list
            if len(user_list) != difficulty:
                print(f"""
Your list of numbers contain {len(user_list)} element, it should contain {difficulty} element!
Unfortionately the requirements were not met. You did't get any points!""")
#                get_data_from_user()
                return False
        check_data_from_user()
        compare_data()
    get_data_from_user()


