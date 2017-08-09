import Tkinter as tk
from PIL import Image, ImageTk
from random import randint

EMPTY = 0
CROSS = 1
NOUGHT = 2
PLAYER_NAMES = ['Nobody', 'Computer', 'Player']    
 
w, h = 3, 3;
Board = [[0 for x in range(w)] for y in range(h)] 

i=0
j=0
while i <= 2:
    while j <= 2:
        Board[i][j] = EMPTY
        j+=1
    j=0
    i+=1
i=0

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

def isWon():
    if Board[0][0] == CROSS and Board[0][1] == CROSS and Board[0][2] == CROSS:
        return CROSS
        
    elif Board[1][0] == CROSS and Board[1][1] == CROSS and Board[1][2] == CROSS:
        return CROSS

    elif Board[2][0] == CROSS and Board[2][1] == CROSS and Board[2][2] == CROSS:
        return CROSS
  
    elif Board[0][0] == CROSS and Board[1][0] == CROSS and Board[2][0] == CROSS:
        return CROSS

    elif Board[0][1] == CROSS and Board[1][1] == CROSS and Board[2][1] == CROSS:
        return CROSS

    elif Board[0][2] == CROSS and Board[1][2] == CROSS and Board[2][2] == CROSS:
        return CROSS

    elif Board[0][0] == CROSS and Board[1][1] == CROSS and Board[2][2] == CROSS:
        return CROSS

    elif Board[2][0] == CROSS and Board[1][1] == CROSS and Board[0][2] == CROSS:
        return CROSS

    elif Board[0][0] == NOUGHT and Board[0][1] == NOUGHT and Board[0][2] == NOUGHT:
        return NOUGHT

    elif Board[1][0] == NOUGHT and Board[1][1] == NOUGHT and Board[1][2] == NOUGHT:
        return NOUGHT

    elif Board[2][0] == NOUGHT and Board[2][1] == NOUGHT and Board[2][2] == NOUGHT:
        return NOUGHT

        
    elif Board[0][0] == NOUGHT and Board[1][0] == NOUGHT and Board[2][0] == NOUGHT:
        return NOUGHT

    elif Board[0][1] == NOUGHT and Board[1][1] == NOUGHT and Board[2][1] == NOUGHT:
        return NOUGHT

    elif Board[0][2] == NOUGHT and Board[1][2] == NOUGHT and Board[2][2] == NOUGHT:
        return NOUGHT

    elif Board[0][0] == NOUGHT and Board[1][1] == NOUGHT and Board[2][2] == NOUGHT:
        return NOUGHT

    elif Board[2][0] == NOUGHT and Board[1][1] == NOUGHT and Board[0][2] == NOUGHT:
        return NOUGHT

    else:
        return EMPTY
    
def announceWinner():
	side = isWon()
	w = tk.Label(root1, text=getPlayerName(side)+' has won.')
	w.pack(side='top')
	disableAllButtons()

def machineMove():
    if Board[0][0] == EMPTY or Board[0][2] == EMPTY or Board[2][0] == EMPTY or Board[2][2] == EMPTY:
            choice1 = randint(0,1)
            choice2 = randint(0,1)
            if choice1 == 1:
                choice1 = 2
            if choice2 == 1:
                choice2 = 2
            while Board[choice1][choice2] !=EMPTY:
                choice1 = randint(0,1)
                choice2 = randint(0,1)
                if choice1 == 1:
                    choice1 = 2
                if choice2 == 1:
                    choice2 = 2
                                        
            Board[choice1][choice2] = CROSS    
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
        
    elif Board[1][1] == EMPTY:
        Board[1][1] = CROSS
        MM.image = Ximage
        MM.configure(image=Ximage)
        MM.config(state='disabled')
    elif Board[1][0] == EMPTY or Board[0][1] == EMPTY or Board[2][1] == EMPTY or Board[1][2] == EMPTY:
        choice1 = randint(0,2)
        choice2 = randint(0,2)
        while Board[choice1][choice2] !=EMPTY:
            choice1 = randint(0,2)
            choice2 = randint(0,2)
        Board[choice1][choice2] = CROSS    
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
    if not isWon():
        garbageVar = 0                     
    else:
        announceWinner()

def callbackTL():
    TL.config(state='disabled')
    imageTL  = Oimage
    TL.image = imageTL
    TL.configure(image=imageTL)
    Board[0][0] = NOUGHT
    if not isWon():
        machineMove()
    else:
		announceWinner()
            
def callbackTM():
    TM.config(state='disabled')
    imageTM  = Oimage
    TM.image = imageTM
    TM.configure(image=imageTM)
    Board[1][0] = NOUGHT
    if not isWon():
        machineMove()
    else:
		announceWinner()
    
def callbackTR():
    TR.config(state='disabled')
    imageTR  = Oimage
    TR.image = imageTR
    TR.configure(image=imageTR)
    Board[2][0] = NOUGHT
    if not isWon():
        machineMove()
    else:
		announceWinner()

def callbackML():
    ML.config(state='disabled')
    imageML  = Oimage
    ML.image = imageML
    ML.configure(image=imageML)
    Board[0][1] = NOUGHT
    if not isWon():
        machineMove()
    else:
		announceWinner()

def callbackMM():
    MM.config(state='disabled')
    imageMM  = Oimage
    MM.image = imageMM
    MM.configure(image=imageMM)
    Board[1][1] = NOUGHT
    if not isWon():
        machineMove()
    else:
		announceWinner()

def callbackMR():
    MR.config(state='disabled')
    imageMR  = Oimage
    MR.image = imageMR
    MR.configure(image=imageMR)
    Board[2][1] = NOUGHT
    
    if not isWon():
        machineMove()
    else:
		announceWinner()
		
def callbackBL():
    BL.config(state='disabled')
    imageBL  = Oimage
    BL.image = imageBL
    BL.configure(image=imageBL)
    Board[0][2] = NOUGHT
    
    if not isWon():
        machineMove()
    else:
		announceWinner()
		
def callbackBM():
    BM.config(state='disabled')
    imageBM = Oimage
    BM.image = imageBM
    BM.configure(image=imageBM)
    Board[1][2] = NOUGHT


    if not isWon():
        machineMove()
    else:
		announceWinner()

def callbackBR():
    BR.config(state='disabled')
    imageBR  = Oimage
    BR.image = imageBR
    BR.configure(image=imageBR)
    Board[2][2] = NOUGHT
    
    if not isWon():
        machineMove()
    else:
		announceWinner()

TL = tk.Button(root1, command=callbackTL)
imageTL = Blankimage
TL.config(image=imageTL)
TL.image = imageTL
TL.grid(column=0, row=0)

TM = tk.Button(root1, command=callbackTM)
imageTM = Blankimage
TM.config(image=imageTM)
TM.image = imageTM
TM.grid(column=1, row=0)

TR = tk.Button(root1, command=callbackTR)
imageTR = Blankimage
TR.config(image=imageTR)
TR.image = imageTR
TR.grid(column=2, row=0)


ML = tk.Button(root1, command=callbackML)
imageML = Blankimage
ML.config(image=imageML)
ML.image = imageML
ML.grid(column=0, row=1)

MM = tk.Button(root1, command=callbackMM)
imageMM = Blankimage
MM.config(image=imageMM)
MM.image = imageTM
MM.grid(column=1, row=1)

MR = tk.Button(root1, command=callbackMR)
imageMR = Blankimage
MR.config(image=imageMR)
MR.image = imageMR
MR.grid(column=2, row=1)


BL = tk.Button(root1, command=callbackBL)
imageBL = Blankimage
BL.config(image=imageBL)
BL.image = imageTL
BL.grid(column=0, row=2)

BM = tk.Button(root1, command=callbackBM)
imageBM = Blankimage
BM.config(image=imageBM)
BM.image = imageBM
BM.grid(column=1, row=2)

BR = tk.Button(root1, command=callbackBR)
imageBR = Blankimage
BR.config(image=imageBR)
BR.image = imageBR
BR.grid(column=2, row=2)



root1.mainloop()