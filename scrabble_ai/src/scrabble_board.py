import random

from scrabble_ai.src.utils import Utils

class ScrabbleBoard:
    def __init__(self):
        self.rows = 15
        self.cols = 15
        self.board = [['_' for _ in range(self.cols)] for _ in range(self.rows)]
        self.multiplier = [[1 for _ in range(self.cols)] for _ in range(self.rows)]

    def make_first_move(self, tiles, dictionary):
        """
        Given tiles, make first move
        :param tiles:
        :return:
        """
        all_subsets = Utils.get_all_subsets(tiles)
        all_subsets.sort(key=len, reverse=True)
        for subset in all_subsets:
            all_valid_permutations = Utils.get_all_valid_permutations(subset, dictionary)
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