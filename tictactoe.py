import Tkinter as tk
from PIL import Image, ImageTk
from random import randint

EMPTY = 0
CROSS = 1
NOUGHT = 2
PLAYER_NAMES = ['Nobody', 'Computer', 'Player']    
WINNING_COMBOS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

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

def isWon(board):
	for combo in WINNING_COMBOS:
		val = board[combo[0]] * board[combo[1]] * board[combo[2]]
		if (val == CROSS**3): return CROSS
		if (val == NOUGHT**3): return NOUGHT
	return EMPTY
    
def announceWinner():
	side = isWon(Board)
	w = tk.Label(root1, text=getPlayerName(side)+' has won.')
	w.pack(side='top')
	disableAllButtons()

def isEmpty(value):
	if value == 'corner':
		return cell(0,0) == EMPTY or cell(0,2) == EMPTY or cell(2,0) == EMPTY or cell(2,2) == EMPTY
	elif value == 'side':
		return cell(1,0) == EMPTY or cell(0,1) == EMPTY or cell(2,1) == EMPTY or cell(1,2) == EMPTY
	elif value == 'center':
		return cell(1,1) == EMPTY
	
	
def machineMove():
    if isEmpty('corner'):
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
        
    elif isEmpty('center'):
        setCell(1,1,CROSS)
    elif isEmpty('side'):
        choice1 = randint(0,2)
        choice2 = randint(0,2)
        while cell(choice1,choice2) !=EMPTY:
            choice1 = randint(0,2)
            choice2 = randint(0,2)
        setCell(choice1, choice2, CROSS)
    if  isWon(Board):
        announceWinner()

def onButtonPress(button, x,y):
    setCell(x,y, NOUGHT)
    if not isWon(Board):
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

if __name__ == '__main__':
	root1.mainloop()