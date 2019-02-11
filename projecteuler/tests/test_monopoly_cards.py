import pytest
from projecteuler.monopoly_cards import Cards



def test_cards():
    expected_choices_list = ['Go', 'Jail', 'C1', 'E3']

    card = Cards(expected_choices_list)

    test = 'Pass'
    test_outcomes=[]

    for x in range(1000):
        card_selected = card.draw()
        test_outcomes.append(card_selected)
    if set(test_outcomes) != set(expected_choices_list):
        test = 'Fail'

    expected_test = 'Pass'

    assert test == expected_test
