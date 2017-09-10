#  File: Bowling.py
#  Description: Calculates the points earned in a bowling game
#  Student's Name: Zi Zhou Wang
#  Student's UT EID: zw3948
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 6/5/2017
#  Date Last Modified: 6/5/2017

#prints the values of the input line
def values(str):
    for i in range(9):
        if str[0] == "X":
            print("X  |", end='')
            str = str[1:len(str)]
        else:
            print(str[0] + " " + str[1] +"|", end='')
            str = str[2:len(str)]
    if len(str) == 2:
        print(str[0] + " " + str[1] + "  |")
    else:
        print(str[0] + " " + str[1] + " " + str[2] + "|")

#calculates and prints the scores of each frame
def scores(str):
    score = 0
    str = str.replace("-", "0")
    ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #prints frames 1 through 9
    for i in range(9):
        if str[0] in ints and str[1] in ints:
            score += int(str[0]) + int(str[1])
            str = str[2:len(str)]
        elif str[1] == "/":
            if str[2] in ints:
                score += 10 + int(str[2])
            else:
                score += 20
            str = str[2:len(str)]
        else:
            if str[2] == "/":
                score += 20
            elif str[1] == "X":
                if str[2] == "X":
                    score += 30
                else:
                    score += 20 + int(str[2])
            else:
                if str[2] == "X":
                    score += 20 + int(str[1])
                else:
                    score += 10 + int(str[1]) + int(str[2])
            str = str[1:len(str)]
        print("%3d|" % score, end='')
    #prints last frame
    if len(str) == 2:
        if str[1] == "/":
            score += 10
        else:
            score += int(str[0]) + int(str[1])
    elif str[1] == "/":
        if str[2] == "X":
            score += 20
        else:
            score += 10 + int(str[2])
    else:
        if str[2] == "/":
            score += 20
        elif str[1] == "X":
            if str[2] == "X":
                score += 30
            else:
                score += 20 + int(str[2])
        else:
            if str[2] == "X":
                score += 20 + int(str[1])
            else:
                score += 10 + int(str[1]) + int(str[2])

    print("%5d|" % score)

def main():
    #reads the file treating each line as a game
    in_file = open("scores.txt", "r")
    for line in in_file:
        line = line.strip()
        line = line.replace(" ", "")
        print("  1   2   3   4   5   6   7   8   9    10")
        print("+---+---+---+---+---+---+---+---+---+-----+")
        print("|", end='')
        values(line)
        print("|", end='')
        scores(line)
        print("+---+---+---+---+---+---+---+---+---+-----+")
        print()
    in_file.close()

main()