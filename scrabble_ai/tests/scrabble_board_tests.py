from scrabble_ai.src.scrabble_board import ScrabbleBoard

class ScrabbleBoardTests:
    def __init__(self):
        pass

    @staticmethod
    def test_make_first_move():
        """
        Given tiles, make first move
        :param tiles:
        :return:
        """
        assert ScrabbleBoard().make_first_move(['a', 'm', 'l', 't', 'e', 'x', 'l'], {'tame', 'mat', 'mate', 'latex'}) == 'latex'

    @staticmethod
    def test_get_points():
        """
        :param start_coordinate:
        :param orientation:
        :param word:
        :return: Points accumulated by input word
        """
        assert True

if __name__ == '__main__':
    ScrabbleBoardTests.test_make_first_move()