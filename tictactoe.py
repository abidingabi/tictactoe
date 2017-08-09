import Tkinter as tk
from PIL import Image, ImageTk
from random import randint

EMPTY = 0
CROSS = 1
NOUGHT = 2
PLAYER_NAMES = ['Nobody', 'Computer', 'Player']    




w, h = 3, 3;
Board = [EMPTY]*9
Buttons = []

root1 = tk.Tk()
root1.title('Tic Tac Toe')
root1.geometry('320x320')

Ximage = ImageTk.PhotoImage(file='.\Images\X Square.png')
Oimage = ImageTk.PhotoImage(file='.\Images\O Square.png')
Blankimage = ImageTk.PhotoImage(file='.\Images\Empty Square.png')

Images = [Blankimage, Ximage, Oimage]

def getPlayerName(side):
	return PLAYER_NAMES[side]
	
def disableAllButtons():
	for x in Buttons:
		x.config(state = 'disabled')  

def cell(x,y): return Board[y*3+x]

def setCell(x,y,value): 
	index = y*3+x
	Board[index] = value
	Buttons[index].image = Images[value]
	Buttons[index].configure(image=Images[value])
	Buttons[index].config(state='disabled')

def multiplyArray(list):
	product = 1
	for x in list:
		product *= x
	return product

def won(x):
	WINNING_COMBOS = [[Board[0],Board[1],Board[2]], [Board[3],Board[4],Board[5]], [Board[6],Board[7],Board[8]], [Board[0],Board[3],Board[6]], [Board[1],Board[4],Board[7]], [Board[2],Board[5],Board[8]], [Board[0],Board[4],Board[8]], [Board[2],Board[4],Board[6]]]
	if multiplyArray(WINNING_COMBOS[0]) == x or multiplyArray(WINNING_COMBOS[1]) == x or multiplyArray(WINNING_COMBOS[2]) == x or multiplyArray(WINNING_COMBOS[2]) == x or multiplyArray(WINNING_COMBOS[3]) == x or multiplyArray(WINNING_COMBOS[4]) == x or multiplyArray(WINNING_COMBOS[5]) == x or multiplyArray(WINNING_COMBOS[6]) == x or multiplyArray(WINNING_COMBOS[7]) == x:
		return True
	else:
		return False
	
def isWon():
	if won(1):
		return CROSS    
	elif won(8):
		return NOUGHT
	else:
		return EMPTY
    
def announceWinner():
	side = isWon()
	w = tk.Label(root1, text=getPlayerName(side)+' has won.')
	w.pack(side='top')
	disableAllButtons()

def machineMove():
    if cell(0,0) == EMPTY or cell(0,2) == EMPTY or cell(2,0) == EMPTY or cell(2,2) == EMPTY:
            choice1 = randint(0,1)
            choice2 = randint(0,1)
            if choice1 == 1:
                choice1 = 2
            if choice2 == 1:
                choice2 = 2
            while cell(choice1,choice2) !=EMPTY:
                choice1 = randint(0,1)
                choice2 = randint(0,1)
                if choice1 == 1:
                    choice1 = 2
                if choice2 == 1:
                    choice2 = 2
                                        
            setCell(choice1,choice2, CROSS)
        
    elif cell(1,1) == EMPTY:
        setCell(1,1,CROSS)
    elif cell(1,0) == EMPTY or cell(0,1) == EMPTY or cell(2,1) == EMPTY or cell(1,2) == EMPTY:
        choice1 = randint(0,2)
        choice2 = randint(0,2)
        while cell(choice1,choice2) !=EMPTY:
            choice1 = randint(0,2)
            choice2 = randint(0,2)
        setCell(choice1, choice2, CROSS)
    if  isWon():
        announceWinner()

def onButtonPress(button, x,y):
    setCell(x,y, NOUGHT)
    if not isWon():
        machineMove()
    else:
		announceWinner()

def createButtons():
	TL = tk.Button(root1, command=lambda: onButtonPress(TL, 0, 0))
	imageTL = Blankimage
	TL.config(image=imageTL)
	TL.image = imageTL
	TL.grid(column=0, row=0)

	TM = tk.Button(root1, command=lambda: onButtonPress(TM, 1, 0))
	imageTM = Blankimage
	TM.config(image=imageTM)
	TM.image = imageTM
	TM.grid(column=1, row=0)

	TR = tk.Button(root1, command=lambda: onButtonPress(TR, 2, 0))
	imageTR = Blankimage
	TR.config(image=imageTR)
	TR.image = imageTR
	TR.grid(column=2, row=0)

	ML = tk.Button(root1, command=lambda: onButtonPress(ML, 0, 1))
	imageML = Blankimage
	ML.config(image=imageML)
	ML.image = imageML
	ML.grid(column=0, row=1)

	MM = tk.Button(root1, command=lambda: onButtonPress(MM, 1, 1))
	imageMM = Blankimage
	MM.config(image=imageMM)
	MM.image = imageTM
	MM.grid(column=1, row=1)

	MR = tk.Button(root1, command=lambda: onButtonPress(MR, 2, 1))
	imageMR = Blankimage
	MR.config(image=imageMR)
	MR.image = imageMR
	MR.grid(column=2, row=1)

	BL = tk.Button(root1, command=lambda: onButtonPress(BL, 0, 2))
	imageBL = Blankimage
	BL.config(image=imageBL)
	BL.image = imageTL
	BL.grid(column=0, row=2)

	BM = tk.Button(root1, command=lambda: onButtonPress(BM, 1, 2))
	imageBM = Blankimage
	BM.config(image=imageBM)
	BM.image = imageBM
	BM.grid(column=1, row=2)

	BR = tk.Button(root1, command=lambda: onButtonPress(BR, 2, 2))
	imageBR = Blankimage
	BR.config(image=imageBR)
	BR.image = imageBR
	BR.grid(column=2, row=2)
	
	return [TL, TM, TR, ML, MM, MR, BL, BM, BR]

Buttons = createButtons()
root1.mainloop()