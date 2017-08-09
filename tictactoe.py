import Tkinter as tk
from PIL import Image, ImageTk
from random import randint
#remove me
EMPTY = 0
CROSS = 1
NOUGHT = 2
PLAYER_NAMES = ['Nobody', 'Computer', 'Player']    
 
w, h = 3, 3;
Board = [EMPTY]*9

root1 = tk.Tk()
root1.title('Tic Tac Toe')
root1.geometry('320x320')

Ximage = ImageTk.PhotoImage(file='.\Images\X Square.png')
Oimage = ImageTk.PhotoImage(file='.\Images\O Square.png')
Blankimage = ImageTk.PhotoImage(file='.\Images\Empty Square.png')

def getPlayerName(side):
	return PLAYER_NAMES[side]
	
def disableAllButtons():
	for x in (TL, TM, TR, ML, MM, MR, BL, BM, BR):
		x.config(state = 'disabled')  

def cell(x,y): return Board[y*3+x]

def setCell(x,y,value): Board[y*3+x] = value

def isWon():
    if cell(0,0) == CROSS and cell(0,1) == CROSS and cell(0,2) == CROSS:
        return CROSS
        
    elif cell(1,0) == CROSS and cell(1,1) == CROSS and cell(1,2) == CROSS:
        return CROSS

    elif cell(2,0) == CROSS and cell(2,1) == CROSS and cell(2,2) == CROSS:
        return CROSS
  
    elif cell(0,0) == CROSS and cell(1,0) == CROSS and cell(2,0) == CROSS:
        return CROSS

    elif cell(0,1) == CROSS and cell(1,1) == CROSS and cell(2,1) == CROSS:
        return CROSS

    elif cell(0,2) == CROSS and cell(1,2) == CROSS and cell(2,2) == CROSS:
        return CROSS

    elif cell(0,0) == CROSS and cell(1,1) == CROSS and cell(2,2) == CROSS:
        return CROSS

    elif cell(2,0) == CROSS and cell(1,1) == CROSS and cell(0,2) == CROSS:
        return CROSS

    elif cell(0,0) == NOUGHT and cell(0,1) == NOUGHT and cell(0,2) == NOUGHT:
        return NOUGHT

    elif cell(1,0) == NOUGHT and cell(1,1) == NOUGHT and cell(1,2) == NOUGHT:
        return NOUGHT

    elif cell(2,0) == NOUGHT and cell(2,1) == NOUGHT and cell(2,2) == NOUGHT:
        return NOUGHT

        
    elif cell(0,0) == NOUGHT and cell(1,0) == NOUGHT and cell(2,0) == NOUGHT:
        return NOUGHT

    elif cell(0,1) == NOUGHT and cell(1,1) == NOUGHT and cell(2,1) == NOUGHT:
        return NOUGHT

    elif cell(0,2) == NOUGHT and cell(1,2) == NOUGHT and cell(2,2) == NOUGHT:
        return NOUGHT

    elif cell(0,0) == NOUGHT and cell(1,1) == NOUGHT and cell(2,2) == NOUGHT:
        return NOUGHT

    elif cell(2,0) == NOUGHT and cell(1,1) == NOUGHT and cell(0,2) == NOUGHT:
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
            if choice1 == 0 and choice2 == 0:
                TL.image = Ximage
                TL.configure(image=Ximage)
                TL.config(state='disabled')
            elif choice1 == 2 and choice2 == 0:
                TR.image = Ximage
                TR.configure(image=Ximage)
                TR.config(state='disabled')
            elif choice1 == 0 and choice2 == 2:
                BL.image = Ximage
                BL.configure(image=Ximage)
                BL.config(state='disabled')
            elif choice1 == 2 and choice2 == 2:
                BR.image = Ximage
                BR.configure(image=Ximage)
                BR.config(state='disabled')
        
    elif cell(1,1) == EMPTY:
        setCell(1,1,CROSS)
        MM.image = Ximage
        MM.configure(image=Ximage)
        MM.config(state='disabled')
    elif cell(1,0) == EMPTY or cell(0,1) == EMPTY or cell(2,1) == EMPTY or cell(1,2) == EMPTY:
        choice1 = randint(0,2)
        choice2 = randint(0,2)
        while cell(choice1,choice2) !=EMPTY:
            choice1 = randint(0,2)
            choice2 = randint(0,2)
        setCell(choice1, choice2, CROSS)
        if choice1 == 1 and choice2 == 0:
            TM.image = Ximage
            TM.configure(image=Ximage)
            TM.config(state='disabled')
        elif choice1 == 0 and choice2 == 1:
            ML.image = Ximage
            ML.configure(image=Ximage)
            ML.config(state='disabled')
        elif choice1 == 2 and choice2 == 1:
            MR.image = Ximage
            MR.configure(image=Ximage)
            MR.config(state='disabled')
        elif choice1 == 1 and choice2 == 2:
            BM.image = Ximage
            BM.configure(image=Ximage)
            BM.config(state='disabled')
    if  isWon():
        announceWinner()

def onButtonPress(button, x,y):
    button.config(state='disabled')
    button.image = Oimage
    button.configure(image=Oimage)
    setCell(x,y, NOUGHT)
    if not isWon():
        machineMove()
    else:
		announceWinner()

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

root1.mainloop()