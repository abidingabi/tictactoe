import unittest
import tictactoe

def board(cells): return tictactoe.Board(cells)

class TicTacToeTest(unittest.TestCase):

	def test_isWon(self):
		_ = tictactoe.EMPTY
		X = tictactoe.CROSS
		O = tictactoe.NOUGHT
		
		self.assertEqual(_, board([_,_,_,
                                   _,_,_,
								   _,_,_]).isWon())

		self.assertEqual(X, board([X,X,X,
		                           _,O,O,
								   _,O,O]).isWon())

		self.assertEqual(X, board([_,O,O,
		                           X,X,X,
								   _,O,O]).isWon())

		self.assertEqual(X, board([_,_,_,
		                           _,_,_,
								   X,X,X]).isWon())

		self.assertEqual(X, board([X,_,_,
		                           X,O,O,
								   X,O,O]).isWon())

		self.assertEqual(X, board([_,X,O,
		                           O,X,O,
								   O,X,_]).isWon())

		self.assertEqual(X, board([_,_,X,
		                           O,O,X,
								   O,O,X]).isWon())
											 
		self.assertEqual(X, board([X,_,O,
		                           O,X,_,
								   O,O,X]).isWon())

		self.assertEqual(X, board([O,_,X,
		                           O,X,_,
								   X,O,O]).isWon())

		self.assertEqual(O, board([O,O,O,
		                           X,X,_,
								   _,_,_]).isWon())

		self.assertEqual(O, board([X,X,_,
		                           O,O,O,
								   _,_,_]).isWon())

		self.assertEqual(O, board([_,X,_,
		                           _,_,X,
								   O,O,O]).isWon())

		self.assertEqual(O, board([O,_,X,
		                           O,X,_,
								   O,_,_]).isWon())

		self.assertEqual(O, board([_,O,X,
		                           _,O,X,
								   _,O,_]).isWon())

		self.assertEqual(O, board([_,_,O,
		                           _,X,O,
								   X,_,O]).isWon())
											 
		self.assertEqual(O, board([O,X,_,
		                           X,O,_,
								   _,_,O]).isWon())

		self.assertEqual(O, board([_,X,O,
		                           _,O,X,
								   O,_,_]).isWon())

		self.assertEqual(_, board([_,X,O,
		                           _,O,X,
								   X,O,O]).isWon())
								   
	def test_move_onEmpty(self):
		_ = tictactoe.EMPTY
		X = tictactoe.CROSS
		O = tictactoe.NOUGHT
	
		board = tictactoe.Board()
		newBoard = board.move(4) # center cells
		self.assertEqual([_]*9, board.cells)
		self.assertEqual([_,_,_, _,O,_, _,_,_], newBoard.cells)
		self.assertEqual(X, newBoard.nextMove)
		
	def test_move_cross(self):
		_ = tictactoe.EMPTY
		X = tictactoe.CROSS
		O = tictactoe.NOUGHT
	
		board = tictactoe.Board()
		newBoard = board.move(4).move(0) # O in the center, X in the top left corner
		self.assertEqual([_]*9, board.cells)
		self.assertEqual([X,_,_, _,O,_, _,_,_], newBoard.cells)
		self.assertEqual(O, newBoard.nextMove)

	def test_move_on_taken_cell(self):
		_ = tictactoe.EMPTY
		X = tictactoe.CROSS
		O = tictactoe.NOUGHT
	
		board = tictactoe.Board()
		newBoard = board.move(4).move(4) # should return None
		
		self.assertEqual(None, newBoard)
		
	def test_build_tree_pre_win(self):
		_ = tictactoe.EMPTY
		X = tictactoe.CROSS
		O = tictactoe.NOUGHT
	
		board = tictactoe.Board([_,O,O,
								 _,O,X,
								 X,_,_])
		board.nextMove = O
		tree = tictactoe.buildGameTree(board)
											 
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TicTacToeTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
