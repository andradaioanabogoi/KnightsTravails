import argparse
import queue


class KnightNode:

    def __init__(self, parent, coordinates):
        self.coordinates = coordinates
        self.children = []
        self.parent = parent
        self.find_children()

    def get_coordinates(self):
        return self.coordinates

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def find_children(self):
        for i in range(1, 9):
            for j in range(1, 9):
                if(is_valid_knight_move(self.coordinates, [i, j]) and valid_coordinates([i, j])):
                    self.children.append([i, j])


def map_letters_to_numbers(input):
    _dict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8
    }
    return _dict[input]


def map_numbers_to_letters(input):
    _dict = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H"
    }
    return _dict[input]


def is_valid_knight_move(start_coordinates, end_coordinates):
    if(abs(end_coordinates[0] - start_coordinates[0]) == 2) and (abs(end_coordinates[1] - start_coordinates[1]) == 1):
        return True
    elif (abs(end_coordinates[0] - start_coordinates[0]) == 1) and (abs(end_coordinates[1] - start_coordinates[1]) == 2):
        return True
    else:
        return False


def valid_coordinates(end_coordinates):
    return (end_coordinates[0] > 0) and (end_coordinates[0] < 9) and (end_coordinates[1] > 0) and (end_coordinates[1] < 9)


def knight_moves(start_coordinates, end_coordinates):
    path = []
    _queue = queue.Queue()
    node = KnightNode(None, start_coordinates)
    _queue.put(node)
    while(_queue.get is not None):
        current_node = _queue.get()
        if current_node.get_coordinates() == end_coordinates:
            while True:
                path.append(current_node.get_coordinates())
                if(current_node.get_parent() is None):
                    break
                current_node = current_node.get_parent()
            return path
        for child in current_node.get_children():
            _queue.put(KnightNode(current_node, child))
    return None


def print_path(path_stack, start_coordinates, end_coordinates):
    if(len(path_stack) == 1):
        print(("It took " + str((len(path_stack)-1)) +
               " moves to traverse from " + start_coordinates + " to " + end_coordinates))
    else:
        print("It took " + str((len(path_stack)-1)) +
              " moves to traverse from " + start_coordinates + " to " + end_coordinates + ". There's the path:")
        path_stack.pop()
        while(True):
            print(encode_chess_notation(path_stack.pop(len(path_stack)-1)), " ")
            if(len(path_stack) == 0):
                break


def decode_chess_notation(chess_notation):
    letter = chess_notation[0]
    return [map_letters_to_numbers(letter), int(chess_notation[1])]


def encode_chess_notation(chess_notation):
    letter = map_numbers_to_letters(chess_notation[0])
    return letter + str(chess_notation[1])


def main(start_coordinates, end_coordinates):

    path_stack = knight_moves(decode_chess_notation(
        start_coordinates), decode_chess_notation(end_coordinates))
    print_path(path_stack, start_coordinates, end_coordinates)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--start',
                        help='The start position of the Knight')
    parser.add_argument('--end',
                        help='The end position of the Knight')
    args = parser.parse_args()

    main(args.start, args.end)
