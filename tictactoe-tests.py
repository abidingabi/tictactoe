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

											 
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TicTacToeTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
