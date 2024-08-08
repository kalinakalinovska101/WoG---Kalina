#in the enxt functions I have created an additional list with the played games
def write_to_file():
    from Live import name
    from Score import current_score
    f = open('Score.txt', 'a')
 #   f.write(f"{current_score } {name}\n")
    f.write(f"{current_score}:{name} \n")
    f.close()
    #This will print for the HTML task
    f = open('Scores.txt', 'a')
    #   f.write(f"{current_score } {name}\n")
    f.write(f"{current_score}:{name} \n")
    f.close()

def delete_extra_entry():
    file = open("Score.txt", 'r+')
    lines = file.readlines()
    # move file pointer to the beginning of a file
    file.seek(0)
    # truncate the file
    file.truncate()
    # start writing lines except the first line
    # lines[1:] from line 2 to last line
    file.writelines(lines[0:8])

def sorting():
    file = open("Score.txt", 'r')
    array1=0
    array2=0
    array3=0
    array1, array2, array3 = [],[],{}
    lines=file.readlines()
    for x in lines:
        fields = x.split(":")
        array1.append(int(fields[0]))
        array2.append(fields[1])
        names=fields[1].replace("\n","")
        array3[int(fields[0])] = names
    array1.sort(reverse=True)
    print("==============================")
    print("    Top Winning Scores")
    print("==============================")
    for x in array1:
        values = array3.get(x)
        print("\n", x, values)
    file.close()