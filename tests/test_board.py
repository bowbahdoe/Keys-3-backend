import unittest
import board

class Test_Board(unittest.TestCase):

    def test_adding_piece(self):
        gameboard = board.Board()

        gameboard.set_piece_at_location((1,0), "arbitrary object")

        self.assertEqual(gameboard.get_piece_at_location((1, 0)), "arbitrary object")

    def test_adding_piece_out_of_bounds(self):
        gameboard = board.Board()

        with self.assertRaises(BufferError):
            gameboard.set_piece_at_location((9, 9), "object")

    def test_getting_piece_at_location(self):
        gameboard = board.Board()

        gameboard.set_piece_at_location((1, 0), "arbitrary object")

        self.assertEqual(gameboard.get_piece_at_location((1, 0)), "arbitrary object")

        gameboard.set_piece_at_location((3, 7), "arbitrary object")

        self.assertEqual(gameboard.get_piece_at_location((3, 7)), "arbitrary object")

    def test_getting_piece_that_is_not_there(self):
        gameboard = board.Board()

        self.assertEqual(gameboard.get_piece_at_location((3, 7)), None)

    def test_is_piece_at_location(self):
        gameboard = board.Board()

        gameboard.set_piece_at_location((1, 0), "arbitrary object")

        self.assertEqual(gameboard.is_piece_at_location((1, 0)), True)

        self.assertEqual(gameboard.is_piece_at_location((1, 1)), False)

    def test_is_location_in_bounds(self):
        gameboard_1 = board.Board()

        #tests diagonals
        for i, e in zip(range(8), range(8)):
            self.assertEqual(gameboard_1.is_location_in_bounds((i, e)), True)

        self.assertEqual(gameboard_1.is_location_in_bounds((1, 8)), False)

        gameboard_2 = board.Board(width=9, height=9)

        for i, e in zip(range(9), range(9)):
            self.assertEqual(gameboard_2.is_location_in_bounds((i, e)), True)

        self.assertEqual(gameboard_2.is_location_in_bounds((9, 9)), False)

    def test_removing_piece(self):
        gameboard = board.Board()

        gameboard.set_piece_at_location((1, 0), "arbitrary object")

        gameboard.remove_piece_at_location((1, 0))
        
        self.assertEqual(gameboard.is_piece_at_location((1, 0)), False)
