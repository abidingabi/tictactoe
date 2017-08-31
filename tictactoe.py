import Tkinter as tk
from PIL import Image, ImageTk
from random import randint
import cPickle as pickle

EMPTY = 0
CROSS = 1
NOUGHT = 2
PLAYER_NAMES = ['Nobody', 'Computer', 'Player']

class Board:
	WINNING_COMBOS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

	def __init__(self, cells = [EMPTY]*9):
		self.cells = cells
		self.nextMove = NOUGHT
		self.rank = 0
		self.children = {}

	def isWon(self):
		for combo in Board.WINNING_COMBOS:
			val = self.cells[combo[0]] * self.cells[combo[1]] * self.cells[combo[2]]
			if (val == CROSS**3): return CROSS
			if (val == NOUGHT**3): return NOUGHT
		return EMPTY
	def cell(self, x,y): return self.cells[y*3+x]


	# creates a new board after "nextMove" party puts a mark at the cell "index"
	def move(self, index):
		if self.cells[index] != EMPTY: return None # the cell is already taken
		result = Board(self.cells[:]) # clone current cells
		result.cells[index] = self.nextMove
		result.nextMove = NOUGHT if self.nextMove == CROSS else CROSS
		return result

def displayMove(index, value):
	buttons[index].image = images[value]
	buttons[index].configure(image=images[value])
	buttons[index].config(state='disabled')

file_name = 'tree.pkl'

# builds game tree; assumes "board" does NOT represent a winning position
def buildGameTree(board):
	treeReadFile = open(file_name, 'r')
	won = board.isWon()
	if won == CROSS: board.rank = 1; return
	if won == NOUGHT: board.rank = -1; return

	for index in range(0,9):
		child = board.move(index)
		if child != None:
			buildGameTree(child)
			board.children[index] = child

	if not board.children: board.rank = 0; return

	childRanks = [child.rank for child in board.children.values()]

	if board.nextMove == CROSS: board.rank = max(childRanks)
	elif board.nextMove == NOUGHT: board.rank = min(childRanks)

currentBoard = Board()
buttons = []

window = tk.Tk()
window.title('Tic Tac Toe')
window.geometry('320x320')

def loadImage(name): return ImageTk.PhotoImage(file='.\Images\\' + name + '.png')
images = [ loadImage('Empty Square'), loadImage('X Square'), loadImage('O Square') ]

def getPlayerName(side):
	return PLAYER_NAMES[side]

def disableAllbuttons():
	for x in buttons:
		x.config(state = 'disabled')



def announceWinner():
	side = currentBoard.isWon()
	w = tk.Label(window, text=getPlayerName(side)+' has won.')
	w.pack(side='top')
	disableAllbuttons()

def isEmpty(value):
	if value == 'corner':
		return currentBoard.cell(0,0) == EMPTY or currentBoard.cell(0,2) == EMPTY or currentBoard.cell(2,0) == EMPTY or currentBoard.cell(2,2) == EMPTY
	elif value == 'side':
		return currentBoard.cell(1,0) == EMPTY or currentBoard.cell(0,1) == EMPTY or currentBoard.cell(2,1) == EMPTY or currentBoard.cell(1,2) == EMPTY
	elif value == 'center':
		return currentBoard.cell(1,1) == EMPTY

def machineMove():
	global currentBoard
	if not currentBoard.children: announceWinner(); return
	index = max(currentBoard.children.iterkeys(), key=(lambda key: currentBoard.children[key].rank))
	currentBoard = currentBoard.children[index]
	displayMove(index, CROSS)
	if currentBoard.isWon(): announceWinner()

def onButtonPress(button, x,y):
	global currentBoard
	index = y*3+x
	currentBoard = currentBoard.children[index]
	displayMove(index, NOUGHT)
	if not currentBoard.isWon(): machineMove()
	else: announceWinner()

def createbuttons():
	TL = tk.Button(window, command=lambda: onButtonPress(TL, 0, 0))
	imageTL = images[EMPTY]
	TL.config(image=imageTL)
	TL.image = imageTL
	TL.grid(column=0, row=0)

	TM = tk.Button(window, command=lambda: onButtonPress(TM, 1, 0))
	imageTM = images[EMPTY]
	TM.config(image=imageTM)
	TM.image = imageTM
	TM.grid(column=1, row=0)

	TR = tk.Button(window, command=lambda: onButtonPress(TR, 2, 0))
	imageTR = images[EMPTY]
	TR.config(image=imageTR)
	TR.image = imageTR
	TR.grid(column=2, row=0)

	ML = tk.Button(window, command=lambda: onButtonPress(ML, 0, 1))
	imageML = images[EMPTY]
	ML.config(image=imageML)
	ML.image = imageML
	ML.grid(column=0, row=1)

	MM = tk.Button(window, command=lambda: onButtonPress(MM, 1, 1))
	imageMM = images[EMPTY]
	MM.config(image=imageMM)
	MM.image = imageTM
	MM.grid(column=1, row=1)

	MR = tk.Button(window, command=lambda: onButtonPress(MR, 2, 1))
	imageMR = images[EMPTY]
	MR.config(image=imageMR)
	MR.image = imageMR
	MR.grid(column=2, row=1)

	BL = tk.Button(window, command=lambda: onButtonPress(BL, 0, 2))
	imageBL = images[EMPTY]
	BL.config(image=imageBL)
	BL.image = imageTL
	BL.grid(column=0, row=2)

	BM = tk.Button(window, command=lambda: onButtonPress(BM, 1, 2))
	imageBM = images[EMPTY]
	BM.config(image=imageBM)
	BM.image = imageBM
	BM.grid(column=1, row=2)

	BR = tk.Button(window, command=lambda: onButtonPress(BR, 2, 2))
	imageBR = images[EMPTY]
	BR.config(image=imageBR)
	BR.image = imageBR
	BR.grid(column=2, row=2)

	return [TL, TM, TR, ML, MM, MR, BL, BM, BR]

buttons = createbuttons()

buildGameTree(currentBoard)

# open the file for writing
fileObject = open(file_name,'wb')
pickle.dump(currentBoard.children, fileObject)

if __name__ == '__main__':
	window.mainloop()
