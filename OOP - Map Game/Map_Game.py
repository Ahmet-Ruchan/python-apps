#Ahmet Ruçhan Avcı

import os
from time import sleep

class Map(object):

    def __init__(self):
        mapList = [[0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0],
                   ["*",0,0,0,0,0,0]]

        self.mapList = mapList

game = Map()

def displayMap():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("This is your map:")
    for i in range(7):
        print(game.mapList[i])
    print("up, down, right, left, quit = 'q'")

    global row
    global column
    for i,j in enumerate(game.mapList):
            for k,player in enumerate(j):
                if player == '*':
                    row = i
                    column = k
                    #print(row,column)
while(1):
    displayMap()
    user = input("=> ")
    if user == 'up':
        a = row - 1 #for 'up'
        if a > 6 or a < 0:
            print("index out of range please wait 3 seconds and continue")
            sleep(3)
            continue
        game.mapList[a][column] = '*'
        game.mapList[row][column] = 0
        displayMap()
    elif user == 'down':
        a = row + 1 #for 'down'
        if a > 6 or a < 0:
            print("index out of range please wait 3 seconds and continue")
            sleep(3)
            continue
        game.mapList[a][column] = '*'
        game.mapList[row][column] = 0
        displayMap()
    elif user == 'right':
        a = column + 1 #for 'right'
        if a > 6 or a < 0:
            print("index out of range please wait 3 seconds and continue")
            sleep(3)
            continue
        game.mapList[row][a] = '*'
        game.mapList[row][column] = 0
        displayMap()
    elif user == 'left':
        a = column - 1 #for 'left'
        if a > 6 or a < 0:
            print("index out of range please wait 3 seconds and continue")
            sleep(3)
            continue
        game.mapList[row][a] = '*'
        game.mapList[row][column] = 0
        displayMap()
    elif user == 'q':
        break
    if game.mapList[0][6] == '*':
        print("You won and game is over!")
        sleep(3)
        break
