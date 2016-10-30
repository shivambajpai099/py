from pygame import mixer
import random# Load the required library


board = ['_','_','_','_','_','_','_','_','_']
winlist = [[0,1,2] ,[0,4,8], [0,3,6], [3,4,5], [6,7,8], [2,5,8], [2,4,6], [1,4,7]]
def showboard(board):
    print board[0] + " | " + board[1] + " | " + board[2]
    print "----------"
    print board[3] + " | " + board[4] + " | " + board[5]
    print "----------"
    print board[6] + " | " + board[7] + " | " + board[8]
    return

def checkuserwin(board,winlist):
    for i in range(0,8):
        wl = winlist[i]
        summ = ord(board[wl[0]]) + ord(board[wl[1]]) + ord(board[wl[2]])
        
        if summ == 264:
            print ("\nUSER WON!!")
            mixer.init()
            mixer.music.load('win.mp3')
            mixer.music.play()
            flag=0
            exit()


def checkcomwin(board,winlist):
    for i in range(0,8):
        wl = winlist[i]
        summ = ord(board[wl[0]]) + ord(board[wl[1]]) + ord(board[wl[2]])
        
        if summ == 237:
            print ("\nCOMPUTER WON!!")
            mixer.init()
            mixer.music.load('lost.mp3')
            mixer.music.play()
            flag=0
            exit()
            
def cominp(board,winlist):
    count(board)
    for i in range(0,8):
        wl = winlist[i]
        summn = ord(board[wl[0]]) + ord(board[wl[1]]) + ord(board[wl[2]])
    
        if summn == 271:
            for k in range(0,3):
                if board[wl[k]] == '_':
                    board[wl[k]] = 'O'
                    return
                
    for i in range(0,8):
        wl = winlist[i]
        summn = ord(board[wl[0]]) + ord(board[wl[1]]) + ord(board[wl[2]])
        
        if summn == 269:
            for k in range(0,3):
                if board[wl[k]] == '_':
                    board[wl[k]] = 'O'
                    return        

    for i in range(0,8):
        wl = winlist[i]
        summn = ord(board[wl[0]]) + ord(board[wl[1]]) + ord(board[wl[2]])
        
        if summn == 253:
            for k in range(0,3):
                if board[wl[k]] == '_':
                    board[wl[k]] = 'O'
                    return
                
    for i in range(0,8):
        if board[i] == '_':
            board[i] = 'O'
            return


def draw():
    print ("\n\nGame Draw")
    exit()

def count(board):
    counting = 0;
    for l in range(0,9):
        if board[l] == '_':
            counting = counting + 1;
    if counting == 0:
        draw()
        
#WELCOME NOTE

showboard(board)
print " "
flag = 1
while flag is 1:
    #userinput
    flag1 = 1
    while flag1 == 1:
        inp = input("\nAt which positon you want to enter : ")
        if board[inp] != '_':
            print "\nInvalid Option"
        else:
            flag1 = 0
    board[inp] = 'X'
    showboard(board)
    print " "
    checkuserwin(board,winlist)
    print "\nComputer's Turn : "
    print " "
    cominp(board,winlist)
    showboard(board)
    checkcomwin(board,winlist)


