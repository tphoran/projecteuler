import string

class TwentyTwo(object):
    """
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over
    five-thousand first names, begin by sorting it into alphabetical order. Then working out the
    alphabetical value for each name, multiply this value by its alphabetical position in the list
    to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 +
    12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 =
    49714.

    What is the total of all the name scores in the file?
    """
    def __init__(self, data_location):
        self.data_location = data_location
        self.letter_values = dict()
        for index, letter in enumerate(string.ascii_uppercase):
            self.letter_values[letter] = index + 1

    def import_data_and_sort_alphabetically(self, data_location):
        f = open(data_location)
        list_of_names_raw = f.read()
        list_of_names_w_quotations = list_of_names_raw.split(',')
        list_of_names = []
        for n in list_of_names_w_quotations:
            list_of_names.append(n[1:-1])
        list_of_names.sort()
        return list_of_names

    def calculate_name_score(self, name, rank):
        sum_of_letter_names = 0
        for c in name:
            sum_of_letter_names += self.letter_values[c]
        solution = sum_of_letter_names * rank
        return solution

    def solve(self):
        ordered_list_of_names = self.import_data_and_sort_alphabetically(self.data_location)
        sum_of_names = 0
        name_rank = 1
        for n in ordered_list_of_names:
            sum_of_names += self.calculate_name_score(n, name_rank)
            name_rank += 1
        return sum_of_names

data_location = '/Users/tphoran/GitHub/projecteuler/projecteuler/twenty_two_input_data.txt'
twenty_two = TwentyTwo(data_location)
print(twenty_two.solve())
