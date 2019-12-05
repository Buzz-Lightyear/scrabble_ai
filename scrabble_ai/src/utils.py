from itertools import permutations

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def get_all_subsets(input):
        """
        Given any list, return all non-empty subsets in the list, sorted by length in reverse order
        :param input:
        :return:
        """
        results = [[]]
        for item in input:
            temp = []
            for result in results:
                temp.append([item] + result)
            results.extend(temp)

        results.remove([])
        return results


    @staticmethod
    def get_all_valid_permutations(input, dictionary):
        """
        Given a list of characters, get all string permutations present in dictionary
        :param input:
        :return:
        """
        return [''.join(p) for p in permutations(''.join(input)) if ''.join(p) in dictionary]

