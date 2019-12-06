import random

from scrabble_ai.src.utils import Utils

class ScrabbleBoard:
    def __init__(self, dictionary=None):
        self.rows = 15
        self.cols = 15
        self.board = [['_' for _ in range(self.cols)] for _ in range(self.rows)]
        self.letter_points = {
            'a': 1,
            'e': 1,
            'i': 1,
            'o': 1,
            'u': 1,
            'l': 1,
            'n': 1,
            's': 1,
            't': 1,
            'r': 1,
            'd': 2,
            'g': 2,
            'b': 3,
            'c': 3,
            'm': 3,
            'p': 3,
            'f': 4,
            'h': 4,
            'v': 4,
            'w': 4,
            'y': 4,
            'k': 5,
            'j': 8,
            'x': 8,
            'q': 10,
            'z': 10,
        }
        self.dictionary = dictionary
        self.premium_tiles = self.set_premium_tiles()

    def set_premium_tiles(self):
        set1 = [(i, i) for i in range(15)]
        set2 = [(i, 14-i) for i in range(15)]
        set3 = [(3, 0), (7, 0), (11, 0), (3, 14), (7, 14), (11, 14)]
        set4 = [(j, i) for (i, j) in set3]
        set5 = [(5, 1), (6, 2), (7, 3), (8, 2), (9, 1), (5, 13), (6, 12), (7, 11), (8, 12), (9, 13)]
        set6 = [(j, i) for (i, j) in set5]

        return set(set1 + set2 + set3 + set4 + set5 + set6)

    def make_first_move(self, tiles):
        """
        Given tiles, make first move
        :param tiles:
        :return:
        """
        all_subsets = Utils.get_all_subsets(tiles)
        all_subsets.sort(key=len, reverse=True)
        for subset in all_subsets:
            all_valid_permutations = Utils.get_all_valid_permutations(subset, self.dictionary)
            if all_valid_permutations:
                return all_valid_permutations[-1]

        return 'a' if 'a' in tiles else None

    def get_points(self, start_coordinate, orientation, word):
        """
        :param start_coordinate:
        :param orientation:
        :param word:
        :return: Points accumulated by input word
        """

        # TO DO: Actual implementation
        return random.choice([1, 2, 3, 4, 5])

    def print_board(self):
        print '\nBoard:\n'
        for row in self.board:
            print ' | '.join(row)