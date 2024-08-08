#name = 'wfejdskl'
#global difficulty
#difficulty = int(3)
#global game

def clear_winning_points():
    global current_score
    current_score = 0
#clear_winning_points()

def add_score():
    from Live import difficulty
    global difficulty
#    difficulty= 3
#    global game
    global current_score
    current_score = (difficulty * 3) + 5 + current_score
    print(f"Your score from the games is: {current_score}")
    input("Press Enter to continue...")
#add_score()

def read_file():
    import os
    SCORES_FILE_NAME = './Scores.txt'
    BAD_RETURN_CODE = -1
    try:
        fr = open(SCORES_FILE_NAME, 'r')
        file_score = fr.read()
        # new_score_w = file_score
#        print("raboti")
        fr.close()
    except:
        file_score = "file not found"
    return file_score

def write_to_scores_file():
    from Live import name, game, difficulty
    f = open('Scores.txt', 'a')
    #   f.write(f"{current_score } {name}\n")
    f.write(f"{current_score}:{name} \n")
    f.close()