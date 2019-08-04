import unittest
from knights_travails import valid_coordinates, is_valid_knight_move, map_letters_to_numbers, print_path, knight_moves


class ValidCoordinates(unittest.TestCase):

    def test_valid_coordinates_valid_values(self):
        res = valid_coordinates([2, 3])
        self.assertEqual(res, True)

    def test_valid_coordinates_x_invalid_y_valid(self):
        res = valid_coordinates([9, 2])
        self.assertEqual(res, False)

    def test_valid_coordinates_x_valid_y_invalid(self):
        res = valid_coordinates([1, 10])
        self.assertEqual(res, False)


class ValidKnightMove(unittest.TestCase):

    def test_valid_knight_move_valid_move(self):
        res = is_valid_knight_move([3, 3], [1, 2])
        self.assertEqual(res, True)

    def test_valid_knight_move_invalid_move(self):
        res = is_valid_knight_move([2, 3], [1, 2])
        self.assertEqual(res, False)


class MapLettersNumbers(unittest.TestCase):

    def test_map_letters_to_numbers(self):
        res = map_letters_to_numbers("A")
        self.assertEqual(res, 1)


class KnightMoves(unittest.TestCase):

    def test_knight_moves(self):
        res = knight_moves([3, 3], [4, 3])
        self.assertEqual(res, [[4, 3], [2, 4], [1, 2], [3, 3]])

    def test_knight_moves_top_left_to_bottom_right(self):
        res = knight_moves([1, 1], [8, 8])
        self.assertEqual(res, [[8, 8], [6, 7], [4, 6], [
                         2, 7], [1, 5], [2, 3], [1, 1]])

    def test_knight_moves_top_left_to_top_right(self):
        res = knight_moves([1, 1], [1, 8])
        self.assertEqual(res, [[1, 8], [2, 6], [3, 4], [1, 5], [2, 3], [1, 1]])

    def test_knight_moves_top_right_to_bottom_left(self):
        res = knight_moves([1, 8], [8, 1])
        self.assertEqual(res, [[8, 1], [6, 2], [4, 1], [
                         2, 2], [1, 4], [2, 6], [1, 8]])


if __name__ == '__main__':
    unittest.main()
