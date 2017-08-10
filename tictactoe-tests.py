import unittest
import tictactoe


class TicTacToeTest(unittest.TestCase):

	def test_isWon(self):
		_ = tictactoe.EMPTY
		X = tictactoe.CROSS
		O = tictactoe.NOUGHT
		
		self.assertEqual(_, tictactoe.isWon([_,_,_,
		                                     _,_,_,
											 _,_,_]))

		self.assertEqual(X, tictactoe.isWon([X,X,X,
		                                     _,O,O,
											 _,O,O]))

		self.assertEqual(X, tictactoe.isWon([_,O,O,
		                                     X,X,X,
											 _,O,O]))

		self.assertEqual(X, tictactoe.isWon([_,_,_,
		                                     _,_,_,
											 X,X,X]))

		self.assertEqual(X, tictactoe.isWon([X,_,_,
		                                     X,O,O,
											 X,O,O]))

		self.assertEqual(X, tictactoe.isWon([_,X,O,
		                                     O,X,O,
											 O,X,_]))

		self.assertEqual(X, tictactoe.isWon([_,_,X,
		                                     O,O,X,
											 O,O,X]))
											 
		self.assertEqual(X, tictactoe.isWon([X,_,O,
		                                     O,X,_,
											 O,O,X]))

		self.assertEqual(X, tictactoe.isWon([O,_,X,
		                                     O,X,_,
											 X,O,O]))

		self.assertEqual(O, tictactoe.isWon([O,O,O,
		                                     X,X,_,
											 _,_,_]))

		self.assertEqual(O, tictactoe.isWon([X,X,_,
		                                     O,O,O,
											 _,_,_]))

		self.assertEqual(O, tictactoe.isWon([_,X,_,
		                                     _,_,X,
											 O,O,O]))

		self.assertEqual(O, tictactoe.isWon([O,_,X,
		                                     O,X,_,
											 O,_,_]))

		self.assertEqual(O, tictactoe.isWon([_,O,X,
		                                     _,O,X,
											 _,O,_]))

		self.assertEqual(O, tictactoe.isWon([_,_,O,
		                                     _,X,O,
											 X,_,O]))
											 
		self.assertEqual(O, tictactoe.isWon([O,X,_,
		                                     X,O,_,
											 _,_,O]))

		self.assertEqual(O, tictactoe.isWon([_,X,O,
		                                     _,O,X,
											 O,_,_]))

		self.assertEqual(_, tictactoe.isWon([_,X,O,
		                                     _,O,X,
											 X,O,O]))

											 
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TicTacToeTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
