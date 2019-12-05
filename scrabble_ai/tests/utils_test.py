from scrabble_ai.src.utils import Utils

class UtilsTest:
    def __init__(self):
        pass

    @staticmethod
    def test_get_all_subsets():
        """
        Test if get_all_subsets from Utils works!
        :param input:
        :return:
        """

        input1 = [1, 2]
        assert Utils.get_all_subsets(input1) == [[1], [2], [2, 1]], 'Something went south!'

        input2 = [1, 1]
        assert Utils.get_all_subsets(input2) == [[1], [1], [1, 1]], 'Something went south!'

        input3 = [1, 1, 2, 2]
        assert Utils.get_all_subsets(input3) == [[1], [1], [1, 1], [2], [2, 1], [2, 1], [2, 1, 1], [2], [2, 1], [2, 1], [2, 1, 1], [2, 2], [2, 2, 1], [2, 2, 1], [2, 2, 1, 1]], 'Something went south!'


    @staticmethod
    def test_get_all_valid_permutations():
        """
        Test get_all_valid_permutations from Utils
        :param input:
        :return:
        """
        assert Utils.get_all_valid_permutations(['a'], {'a'}) == ['a']

        assert Utils.get_all_valid_permutations(['a', 'b', 't', 'c', 'h'], {'batch', 'bat', 'cat', 'hat'}) == ['batch']

if __name__ == '__main__':
    UtilsTest.test_get_all_subsets()
    UtilsTest.test_get_all_valid_permutations()