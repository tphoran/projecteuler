class Eighteen(object):
    """
    By starting at the top of the triangle below and moving to adjacent numbers on the row below,
    the maximum total from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.
    """

    def __init__(self, input_string):
        self.input_string = input_string

    def transform_string_to_list_of_integers(self, input_sting):
        string_to_list = input_sting.split()
        number_list = []
        for i in string_to_list:
            number_list.append(int(i))
        return number_list

    def create_triangle_levels(self, input_string):
        number_list = self.transform_string_to_list_of_integers(input_string)
        start_of_level = 0
        end_of_level = 1
        size_of_level = 1
        list_of_levels = []
        while start_of_level < len(number_list):
            list_of_levels.append(number_list[start_of_level:end_of_level])
            start_of_level = end_of_level
            size_of_level += 1
            end_of_level += size_of_level
        return list_of_levels

    def collect_best_possible_outcomes_from_two_levels(self, level_one, level_two):
        outcomes = []
        for n in range(len(level_one)):
            outcomes.append(level_one[n]+level_two[n])
            outcomes.append(level_one[n] + level_two[n+1])

        best_outcomes = [outcomes[0],]
        for o in range(1, len(outcomes)-2, 2):
            best_outcomes.append(max(outcomes[o], outcomes[o+1]))
        best_outcomes.append(outcomes[len(outcomes)-1])
        return best_outcomes

    def solve(self):
        list_of_levels = self.create_triangle_levels(self.input_string)
        running_outcomes = list_of_levels[0]
        for l in list_of_levels[1:]:
            running_outcomes = self.collect_best_possible_outcomes_from_two_levels(running_outcomes,
                                                                                   l)
        return max(running_outcomes)


euler_string = '75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 ' \
               '07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 ' \
               '32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 ' \
               '68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 ' \
               '16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

eighteen = Eighteen(euler_string)
print(eighteen.solve())
