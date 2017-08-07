import Tkinter as tk
from PIL import Image, ImageTk
from random import randint

w, h = 3, 3;
Board = [[0 for x in range(w)] for y in range(h)] 

i=0
j=0
while i <= 2:
    while j <= 2:
        Board[i][j] = ''
        j+=1
    j=0
    i+=1
i=0

def isWon():
    if Board[0][0] == 'X' and Board[0][1] == 'X' and Board[0][2] == 'X':
        return 'AI'
        
    elif Board[1][0] == 'X' and Board[1][1] == 'X' and Board[1][2] == 'X':
        return 'AI'

    elif Board[2][0] == 'X' and Board[2][1] == 'X' and Board[2][2] == 'X':
        return 'AI'
  
    elif Board[0][0] == 'X' and Board[1][0] == 'X' and Board[2][0] == 'X':
        return 'AI'

    elif Board[0][1] == 'X' and Board[1][1] == 'X' and Board[2][1] == 'X':
        return 'AI'

    elif Board[0][2] == 'X' and Board[1][2] == 'X' and Board[2][2] == 'X':
        return 'AI'

    elif Board[0][0] == 'X' and Board[1][1] == 'X' and Board[2][2] == 'X':
        return 'AI'

    elif Board[2][0] == 'X' and Board[1][1] == 'X' and Board[0][2] == 'X':
        return 'AI'

    elif Board[0][0] == 'O' and Board[0][1] == 'O' and Board[0][2] == 'O':
        return 'Player'

    elif Board[1][0] == 'O' and Board[1][1] == 'O' and Board[1][2] == 'O':
        return 'Player'

    elif Board[2][0] == 'O' and Board[2][1] == 'O' and Board[2][2] == 'O':
        return 'Player'

        
    elif Board[0][0] == 'O' and Board[1][0] == 'O' and Board[2][0] == 'O':
        return 'Player'

    elif Board[0][1] == 'O' and Board[1][1] == 'O' and Board[2][1] == 'O':
        return 'Player'

    elif Board[0][2] == 'O' and Board[1][2] == 'O' and Board[2][2] == 'O':
        return 'Player'

    elif Board[0][0] == 'O' and Board[1][1] == 'O' and Board[2][2] == 'O':
        return 'Player'

    elif Board[2][0] == 'O' and Board[1][1] == 'O' and Board[0][2] == 'O':
        return 'Player'

    else:
        return False
    

def machineMove():
    Ximage = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\X Square.png')
    if Board[0][0] == '' or Board[0][2] == '' or Board[2][0] == '' or Board[2][2] == '':
            choice1 = randint(0,1)
            choice2 = randint(0,1)
            if choice1 == 1:
                choice1 = 2
            if choice2 == 1:
                choice2 = 2
            while Board[choice1][choice2] !='':
                choice1 = randint(0,1)
                choice2 = randint(0,1)
                if choice1 == 1:
                    choice1 = 2
                if choice2 == 1:
                    choice2 = 2
                                        
            Board[choice1][choice2] = 'X'    
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
        
    elif Board[1][1] == '':
        Board[1][1] = 'X'
        MM.image = Ximage
        MM.configure(image=Ximage)
        MM.config(state='disabled')
    elif Board[1][0] == '' or Board[0][1] == '' or Board[2][1] == '' or Board[1][2] == '':
        choice1 = randint(0,2)
        choice2 = randint(0,2)
        while Board[choice1][choice2] !='':
            choice1 = randint(0,2)
            choice2 = randint(0,2)
        Board[choice1][choice2] = 'X'    
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
        garbageVar=0
                                
    else:
        w = tk.Label(root1, text=str(isWon()+' has won.'))
        w.pack(side='top')
                                                        
                
                                

root1 = tk.Tk()
root1.title('Tic Tac Toe')
root1.geometry('320x320')

def callbackTL():
    TL.config(state='disabled')
    imageTL  = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\O Square.png')
    TL.image = imageTL
    TL.configure(image=imageTL)
    Board[0][0] = 'O'
    if not isWon():
        machineMove()
    else:
        for x in (TL, TM, TR, ML, MM, MR, BL, BM, BR):
            x.config(state = 'disabled')

        w = tk.Label(root1, text=str(isWon()+' has won.'))
        w.pack(side='top')
            
def callbackTM():
    TM.config(state='disabled')
    imageTM  = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\O Square.png')
    TM.image = imageTM
    TM.configure(image=imageTM)
    Board[1][0] = 'O'
    if not isWon():
        machineMove()
    
    else:
        for x in (TL, TM, TR, ML, MM, MR, BL, BM, BR):
            x.config(state = 'disabled')

        w = tk.Label(root1, text=str(isWon()+' has won.'))
        w.pack(side='top')

    
def callbackTR():
    TR.config(state='disabled')
    imageTR  = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\O Square.png')
    TR.image = imageTR
    TR.configure(image=imageTR)
    Board[2][0] = 'O'
    if not isWon():
        machineMove()
    
    else:
        for x in (TL, TM, TR, ML, MM, MR, BL, BM, BR):
            x.config(state = 'disabled')

        w = tk.Label(root1, text=str(isWon()+' has won.'))
        w.pack(side='top')

def callbackML():
    ML.config(state='disabled')
    imageML  = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\O Square.png')
    ML.image = imageML
    ML.configure(image=imageML)
    Board[0][1] = 'O'
    if not isWon():
        machineMove()
    else:
        for x in (TL, TM, TR, ML, MM, MR, BL, BM, BR):
            x.config(state = 'disabled')

        w = tk.Label(root1, text=str(isWon()+' has won.'))
        w.pack(side='top')

def callbackMM():
    MM.config(state='disabled')
    imageMM  = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\O Square.png')
    MM.image = imageMM
    MM.configure(image=imageMM)
    Board[1][1] = 'O'
    if not isWon():
        machineMove()
    
    else:
        for x in (TL, TM, TR, ML, MM, MR, BL, BM, BR):
            x.config(state = 'disabled')

        w = tk.Label(root1, text=str(isWon()+' has won.'))
        w.pack(side='top')

def callbackMR():
    MR.config(state='disabled')
    imageMR  = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\O Square.png')
    MR.image = imageMR
    MR.configure(image=imageMR)
    Board[2][1] = 'O'
    
    if not isWon():
        machineMove()
    else:
        for x in (TL, TM, TR, ML, MM, MR, BL, BM, BR):
            x.config(state = 'disabled')

        w = tk.Label(root1, text=str(isWon()+' has won.'))
        w.pack(side='top')

def callbackBL():
    BL.config(state='disabled')
    imageBL  = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\O Square.png')
    BL.image = imageBL
    BL.configure(image=imageBL)
    Board[0][2] = 'O'
    
    if not isWon():
        machineMove()
    else:
        for x in (TL, TM, TR, ML, MM, MR, BL, BM, BR):
            x.config(state = 'disabled')

        w = tk.Label(root1, text=str(isWon()+' has won.'))
        w.pack(side='top')

def callbackBM():
    BM.config(state='disabled')
    imageBM = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\O Square.png')
    BM.image = imageBM
    BM.configure(image=imageBM)
    Board[1][2] = 'O'


    if not isWon():
        machineMove()
    else:
        for x in (TL, TM, TR, ML, MM, MR, BL, BM, BR):
            x.config(state = 'disabled')

        w = tk.Label(root1, text=str(isWon()+' has won.'))
        w.pack(side='top')

def callbackBR():
    BR.config(state='disabled')
    imageBR  = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\O Square.png')
    BR.image = imageBR
    BR.configure(image=imageBR)
    Board[2][2] = 'O'
    
    if not isWon():
        machineMove()
    else:
        for x in (TL, TM, TR, ML, MM, MR, BL, BM, BR):
            x.config(state = 'disabled')
        w = tk.Label(root1, text=str(isWon()+' has won.'))
        w.pack(side='top')


TL = tk.Button(root1, command=callbackTL)
imageTL = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\Empty Square.png')
TL.config(image=imageTL)
TL.image = imageTL
TL.grid(column=0, row=0)

TM = tk.Button(root1, command=callbackTM)
imageTM = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\Empty Square.png')
TM.config(image=imageTM)
TM.image = imageTM
TM.grid(column=1, row=0)

TR = tk.Button(root1, command=callbackTR)
imageTR = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\Empty Square.png')
TR.config(image=imageTR)
TR.image = imageTR
TR.grid(column=2, row=0)


ML = tk.Button(root1, command=callbackML)
imageML = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\Empty Square.png')
ML.config(image=imageML)
ML.image = imageML
ML.grid(column=0, row=1)

MM = tk.Button(root1, command=callbackMM)
imageMM = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\Empty Square.png')
MM.config(image=imageMM)
MM.image = imageTM
MM.grid(column=1, row=1)

MR = tk.Button(root1, command=callbackMR)
imageMR = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\Empty Square.png')
MR.config(image=imageMR)
MR.image = imageMR
MR.grid(column=2, row=1)


BL = tk.Button(root1, command=callbackBL)
imageBL = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\Empty Square.png')
BL.config(image=imageBL)
BL.image = imageTL
BL.grid(column=0, row=2)

BM = tk.Button(root1, command=callbackBM)
imageBM = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\Empty Square.png')
BM.config(image=imageBM)
BM.image = imageBM
BM.grid(column=1, row=2)

BR = tk.Button(root1, command=callbackBR)
imageBR = ImageTk.PhotoImage(file='C:\Users\dansm\Desktop\Folders\Programming\Python\Tkinkter\Images\Empty Square.png')
BR.config(image=imageBR)
BR.image = imageBR
BR.grid(column=2, row=2)



root1.mainloop()