#This will create a page over 127.0.0.1:500 to see the result

from flask import Flask
app = Flask(__name__)
import os
SCORES_FILE_NAME = './Scores.txt'
fr = open(SCORES_FILE_NAME, 'r')
global file_score
file_score = fr.read()
    # new_score_w = file_score
fr.close()


@app.route('/')
def worldOfGame():
    score = file_score
#    score = str('test')
    print(score)
    if score:
        massage = "<html> <head> <title>Scores Game</title> </head> <body> <h1>The score is : <div id='score'>" + score + "</div></h1> </body></html>"
    else :
        errorMassage = "<html> <head> <title>Scores Game</title> </head> <body> <h1><div id='score' style='color:red'>" + score + "</div></h1> </body></html>"
    return massage
worldOfGame()

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0')
worldOfGame()



