import pytest
import re
import inspect
import os
import session6
import test_session6

README_CONTENT_CHECK_FOR = [
        'random',
        'suits',
        'cards',
        'deck',
        'deck_generator_lmz',
        'deck_generator',
        'card_dealer',
        'royalflush',
        'straightflush',
        'fourofakind',
        'fullhouse',
        'flush',
        'straight',
        'threeofakind',
        'twopair',
        'onepair',
        'highcard',
        'tiebreaker',
        'rank',
        'poker_2_player',
        'Value Error'
        ]

# predefined deck
deck = {('6', 'hearts'), ('7', 'diamonds'), ('9', 'diamonds'), ('king', 'diamonds'), ('5', 'diamonds'), ('3', 'diamonds'), ('10', 'hearts'), ('2', 'hearts'), ('6', 'clubs'), ('10', 'clubs'), ('jack', 'diamonds'), ('king', 'spades'), ('ace', 'hearts'), ('2', 'clubs'), ('8', 'clubs'), ('jack', 'hearts'), ('7', 'clubs'), ('2', 'diamonds'), ('10', 'diamonds'), ('jack', 'clubs'), ('ace', 'clubs'), ('9', 'spades'), ('8', 'hearts'), ('5', 'spades'), ('6', 'diamonds'), ('7', 'hearts'), ('8', 'diamonds'), ('4', 'spades'), ('10', 'spades'), ('queen', 'diamonds'), ('6', 'spades'), ('4', 'hearts'), ('3', 'clubs'), ('ace', 'diamonds'), ('queen', 'spades'), ('9', 'clubs'), ('4', 'clubs'), ('5', 'clubs'), ('3', 'hearts'), ('jack', 'spades'), ('5', 'hearts'), ('8', 'spades'), ('king', 'hearts'), ('4', 'diamonds'), ('ace', 'spades'), ('7', 'spades'), ('9', 'hearts'), ('king', 'clubs'), ('queen', 'hearts'), ('3', 'spades'), ('queen', 'clubs'), ('2', 'spades')}

# types of suits
suits = {'spades', 'clubs', 'hearts', 'diamonds'}
# types of cards
cards = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'}

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_count():
    functions = inspect.getmembers(test_session6, inspect.isfunction)
    assert len(functions) > 25, 'Test cases seems to be low. Work harder man...'

def test_function_repeatations():
    functions = inspect.getmembers(test_session6, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'

def test_deck_lmz():
    assert session6.deck_generator_lmz(suits, cards) == deck , 'Incorrect cards using LMZ operation'
    assert len(session6.deck_generator_lmz(suits, cards)) == 52, 'Incorrect number of cards using LMZ operation'

def test_deck():
    assert session6.deck_generator(suits, cards) == deck , 'Incorrect cards using normal operation'
    assert len(session6.deck_generator(suits, cards)) == 52, 'Incorrect number of cards using normal operation'

#game with random card count pick
def test_poker_2_player():
    for i in range(200):
        card_count, deal = session6.card_dealer(suits, cards)
        assert "Player" in session6.poker_2_player(card_count, deal), 'your poker game fails somewhere...'

def test_royal_flush():
    hand = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    assert session6.royalflush(hand)[0] == 'royal_flush', 'royal_flush hand check failed'

def test_straight_flush():
    hand = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    assert session6.straightflush(hand)[0] == 'straight_flush', 'straight_flush hand check failed'

def test_four_of_a_kind():
    hand = [('7', 'hearts'), ('7', 'diamonds'), ('7', 'spades'), ('7', 'hearts'), ('10', 'spades')]
    assert session6.fourofakind(hand)[0] == 'four_of_a_kind', 'four_of_a_kind hand check failed'

def test_full_house():
    hand = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'spades'), ('king', 'diamonds')]
    assert session6.fullhouse(hand)[0] == 'full_house', 'full_house hand check failed'

def test_flush():
    hand =  [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    assert session6.flush(hand)[0] == 'flush', 'flush hand check failed'

def test_straight():
    hand = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    assert session6.straight(hand)[0] == 'straight', 'straight hand check failed'

def test_three_of_a_kind():
    hand = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    assert session6.threeofakind(hand)[0] == 'three_of_a_kind', 'three_of_a_kind hand check failed'

def test_two_pair():
    hand = [('king', 'hearts'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    assert session6.twopair(hand)[0] == 'two_pair', 'two_pair hand check failed'

def test_one_pair():
    hand = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'clubs'), ('10', 'spades')]
    assert session6.onepair(hand)[0] == 'one_pair', 'one_pair hand check failed'

def test_high_card():
    hand = [('9', 'spades'), ('queen', 'diamonds'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert session6.highcard(hand)[0] == 'high_card', 'high_card hand check failed'

def test_poker5_rf_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    player_B = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    assert "Draw" in session6.poker_2_player(5, [player_A,player_B]),"Royal Flush should be a draw"

def test_poker4_rf_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
    assert "Draw" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should be a draw"

def test_poker3_rf_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')]
    player_B = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades')]
    assert "Draw" in session6.poker_2_player(3, [player_A,player_B]),"Royal Flush should be a draw"

def test_poker5_rf_sf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    player_B = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Royal Flush should win"

def test_poker4_rf_sf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('10', 'spades'), ('9', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should win"

def test_poker3_rf_sf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')]
    player_B = [('jack', 'spades'), ('10', 'spades'), ('queen', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Royal Flush should win"

def test_poker4_rf_fk():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('7', 'hearts'), ('7', 'diamonds'), ('7', 'spades'), ('7', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should win"

def test_poker5_rf_f():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Royal Flush should win"

def test_poker4_rf_f():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should win"

def test_poker3_rf_f():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Royal Flush should win"

def test_poker4_rf_s():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should win"

def test_poker3_rf_s():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')]
    player_B = [('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Royal Flush should win"

def test_poker3_rf_op():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')]
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Royal Flush should win"

def test_poker4_rf_hc():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('9', 'spades'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should win"

def test_poker3_rf_hc():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')]
    player_B = [('9', 'spades'), ('king', 'diamonds'), ('queen', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Royal Flush should win"

def test_poker5_sf_rf():
    player_A = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Royal Flush should win"

def test_poker4_sf_rf():
    player_A = [('10', 'spades'), ('9', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
    player_B = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should win"

def test_poker3_sf_rf():
    player_A = [('jack', 'spades'), ('10', 'spades'), ('queen', 'spades')]
    player_B = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Royal Flush should win"

def test_poker5_sf_sf():
    player_A = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('9', 'hearts'), ('8', 'hearts'), ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    assert "Draw" in session6.poker_2_player(5, [player_A,player_B]),"Straight Flush should be a draw"

def test_poker4_sf_sf():
    player_A = [('9', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('9', 'hearts'), ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]

    assert "Draw" in session6.poker_2_player(4, [player_A,player_B]),"Straight Flush should be a draw"

def test_poker3_sf_sf():
    player_A = [('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    assert "Draw" in session6.poker_2_player(3, [player_A,player_B]),"Straight Flush should be a draw"

def test_poker5_sf_fh():
    player_A = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('ace', 'diamonds'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'clubs'), ('king', 'diamonds')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Straight Flush should win"

def test_poker5_sf_f():
    player_A = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('5', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Straight Flush should win"

def test_poker4_sf_f():
    player_A = [('9', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('7', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Straight Flush should win"

def test_poker3_sf_f():
    player_A = [('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('5', 'spades'), ('2', 'spades'), ('3', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Straight Flush should win"

def test_poker5_sf_s():
    player_A = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'clubs'), ('jack', 'clubs'), ('10', 'hearts')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Straight Flush should win"

def test_poker4_sf_s():
    player_A = [('9', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('king', 'diamonds'), ('queen', 'clubs'), ('jack', 'clubs'), ('10', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Straight Flush should win"

def test_poker3_sf_s():
    player_A = [('10', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
    player_B = [('king', 'diamonds'), ('queen', 'clubs'), ('jack', 'clubs')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Straight should win"

def test_poker5_sf_tk():
    player_A = [('9', 'hearts'), ('8', 'clubs'), ('queen', 'spades'), ('jack', 'diamonds'), ('10', 'hearts')]
    player_B = [('queen', 'hearts'), ('queen', 'diamonds'), ('queen', 'clubs'), ('jack', 'hearts'), ('10', 'clubs')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Straight Flush should win"

def test_poker3_sf_tk():
    player_A = [('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('queen', 'hearts'), ('queen', 'diamonds'), ('queen', 'clubs')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Straight Flush should win"

def test_poker4_sf_tp():
    player_A = [('9', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('queen', 'clubs'), ('queen', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Straight Flush should win"

def test_poker5_sf_op():
    player_A = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('king', 'clubs'), ('king', 'diamonds'), ('jack', 'diamonds'), ('queen', 'hearts'), ('10', 'clubs')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Straight Flush should win"

def test_poker4_sf_op():
    player_A = [('9', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('king', 'clubs'), ('king', 'diamonds'), ('jack', 'diamonds'), ('queen', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Straight Flush should win"

def test_poker3_sf_op():
    player_A = [('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('king', 'clubs'), ('king', 'diamonds'), ('jack', 'diamonds')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Straight Flush should win"

def test_poker5_sf_hc():
    player_A = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('9', 'diamonds'), ('king', 'diamonds'), ('5', 'diamonds'), ('jack', 'clubs'), ('10', 'hearts')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Straight Flush should win"

def test_poker4_sf_hc():
    player_A = [('9', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('9', 'diamonds'), ('king', 'diamonds'), ('queen', 'diamonds'), ('jack', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Straight Flush should win"

def test_poker3_sf_hc():
    player_A = [('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('9', 'spades'), ('king', 'diamonds'), ('queen', 'diamonds')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Straight Flush should win"

def test_poker4_fk_rf():
    player_A = [('10', 'spades'), ('9', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
    player_B = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should win"

def test_poker5_fh_sf():
    player_A = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'spades'), ('king', 'diamonds')]
    player_B = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Straight flush should win"

def test_poker5_fh_fh_B():
    player_B = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'spades'), ('king', 'diamonds')]
    player_A = [('queen', 'diamonds'), ('queen', 'clubs'), ('8', 'clubs'), ('8', 'spades'), ('8', 'diamonds')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Full House B should win"

def test_poker5_fh_fh_A():
    player_A = [('ace', 'spades'), ('ace', 'hearts'), ('king', 'clubs'), ('king', 'spades'), ('king', 'diamonds')]
    player_B = [('ace', 'clubs'), ('ace', 'diamonds'), ('queen', 'clubs'), ('queen', 'spades'), ('queen', 'diamonds')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Full House A should win"

def test_poker5_fh_f():
    player_A = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'spades'), ('king', 'diamonds')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Full House should win"

def test_poker5_fh_tk():
    player_A = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'spades'), ('king', 'diamonds')]
    player_B = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Full House should win"

def test_poker5_fh_tp():
    player_A = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'spades'), ('king', 'diamonds')]
    player_B = [('king', 'hearts'), ('king', 'clubs'), ('queen', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Full House should win"

def test_poker5_f_rf():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Royal Flush should win"

def test_poker4_f_rf():
    player_A = [('9', 'spades'), ('2', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should win"

def test_poker3_f_rf():
    player_A = [('9', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Royal Flush should win"

def test_poker3_f_sf():
    player_A =[('9', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('jack', 'spades'), ('10', 'spades'), ('queen', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Straight flush should win"

def test_poker5_f_fh():
    player_A = [('9', 'spades'), ('2', 'spades'), ('4', 'spades'), ('7', 'spades'), ('3', 'spades')]
    player_B = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'spades'), ('king', 'diamonds')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Full House should win"

def test_poker5_f_f_A():
    player_A = [('10', 'spades'), ('2', 'spades'), ('3', 'spades'), ('5', 'spades'), ('7', 'spades')]
    player_B = [('9', 'hearts'), ('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts'), ('7', 'hearts')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Flush A should win"

def test_poker5_f_f_B():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('10', 'hearts'), ('2', 'hearts'), ('3', 'hearts'), ('5', 'hearts'), ('7', 'hearts')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Flush B should win"

def test_poker5_f_f():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('9', 'hearts'), ('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts'), ('7', 'hearts')]
    assert "Draw" in session6.poker_2_player(5, [player_A,player_B]),"Flush should be a draw"

def test_poker4_f_f_A():
    player_A = [('10', 'spades'), ('2', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('9', 'hearts'), ('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Flush A should win"

def test_poker4_f_f_B():
    player_A = [('9', 'spades'), ('2', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('10', 'hearts'), ('2', 'hearts'), ('8', 'hearts'), ('4', 'hearts')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Flush B should win"

def test_poker4_f_f():
    player_A = [('9', 'spades'), ('2', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('9', 'hearts'), ('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Flush A should win"

def test_poker3_f_f_A():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades')]
    player_B = [('8', 'hearts'), ('2', 'hearts'), ('3', 'hearts')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Flush A should win"

def test_poker3_f_f_B():
    player_A = [('8', 'spades'), ('2', 'spades'), ('3', 'spades')]
    player_B = [('9', 'hearts'), ('2', 'hearts'), ('3', 'hearts')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Flush B should win"

def test_poker3_f_f():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades')]
    player_B = [('9', 'hearts'), ('2', 'hearts'), ('3', 'hearts')]
    assert "Draw" in session6.poker_2_player(3, [player_A,player_B]),"Flush should be a draw"

def test_poker5_f_s():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Flush should win"

def test_poker4_f_s():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades')]
    player_B = [('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Flush should win"

def test_poker3_f_s():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades')]
    player_B = [('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Flush should win"

def test_poker5_f_tk():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Flush should win"

def test_poker4_f_tk():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades')]
    player_B = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Flush should win"

def test_poker3_f_tk():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades')]
    player_B = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Flush should win"

def test_poker5_f_tp():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Flush should win"

def test_poker4_f_tp():
    player_A =[('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Flush should win"

def test_poker5_f_op():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Flush should win"

def test_poker4_f_op():
    player_A =[('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades')]
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Flush should win"

def test_poker3_f_op():
    player_A =[('9', 'spades'), ('2', 'spades'), ('3', 'spades')]
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Flush should win"

def test_poker5_s_sf():
    player_A = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'diamonds'), ('jack', 'clubs'), ('10', 'hearts')]
    player_B = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Straight flush should win"

def test_poker4_s_sf():
    player_A = [('9', 'clubs'),  ('queen', 'clubs'), ('jack', 'diamonds'), ('10', 'hearts')]
    player_B = [('10', 'spades'), ('9', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Straight flush should win"

def test_poker3_s_sf():
    player_A = [('queen', 'clubs'), ('jack', 'clubs'), ('10', 'hearts')]
    player_B = [('jack', 'spades'), ('10', 'spades'), ('queen', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Straight flush should win"

def test_poker5_s_fk():
    player_A = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('7', 'hearts'), ('7', 'diamonds'), ('7', 'spades'), ('7', 'clubs'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"4 of a kind should win"

def test_poker4_s_fk():
    player_A = [('9', 'clubs'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('7', 'hearts'), ('7', 'diamonds'), ('7', 'spades'), ('7', 'clubs')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"4 of a kind should win"

def test_poker5_s_fh():
    player_A = [('9', 'clubs'), ('king', 'clubs'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'spades'), ('king', 'diamonds')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Full House should win"

def test_poker5_s_f():
    player_A = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Flush should win"

def test_poker4_s_f():
    player_A = [('9', 'clubs'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Flush should win"

def test_poker3_s_f():
    player_A = [('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Flush should win"

def test_poker5_s_s():
    player_A = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('9', 'hearts'), ('king', 'clubs'), ('queen', 'diamonds'), ('jack', 'hearts'), ('10', 'spades')]
    assert "Draw" in session6.poker_2_player(5, [player_A,player_B]),"Straight should be a draw"

def test_poker4_s_s_A():
    player_A = [('king', 'clubs'), ('queen', 'spades'), ('jack', 'hearts'), ('10', 'hearts')]
    player_B = [('9', 'diamonds'), ('queen', 'hearts'), ('jack', 'spades'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Straight A should win"

def test_poker4_s_s_B():
    player_B = [('king', 'clubs'), ('queen', 'spades'), ('jack', 'hearts'), ('10', 'hearts')]
    player_A = [('9', 'diamonds'), ('queen', 'hearts'), ('jack', 'spades'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Straight B should win"

def test_poker4_s_s():
    player_A = [('king', 'clubs'), ('queen', 'spades'), ('jack', 'hearts'), ('10', 'hearts')]
    player_B = [('king', 'diamonds'), ('queen', 'hearts'), ('jack', 'spades'), ('10', 'spades')]
    assert "Draw" in session6.poker_2_player(4, [player_A,player_B]),"Straight should be draw"

def test_poker3_s_s_A():
    player_A = [('queen', 'clubs'), ('jack', 'diamonds'), ('king', 'hearts')]
    player_B = [('10', 'diamonds'), ('queen', 'spades'), ('jack', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Straight A should win"

def test_poker3_s_s_B():
    player_B = [('queen', 'clubs'), ('jack', 'diamonds'), ('king', 'hearts')]
    player_A = [('10', 'diamonds'), ('queen', 'spades'), ('jack', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Straight B should win"

def test_poker3_s_s():
    player_A = [('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades')]
    player_B = [('king', 'hearts'), ('queen', 'diamonds'), ('jack', 'clubs')]
    assert "Draw" in session6.poker_2_player(3, [player_A,player_B]),"Straight should be a draw"

def test_poker4_s_tk():
    player_A = [('9', 'clubs'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('queen', 'hearts'), ('queen', 'diamonds'), ('queen', 'clubs'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Straight should win"

def test_poker3_s_tk():
    player_A = [('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('queen', 'hearts'), ('queen', 'diamonds'), ('queen', 'clubs')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Straight should win"

def test_poker5_s_tp():
    player_A = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('queen', 'diamonds'), ('queen', 'hearts'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Straight should win"

def test_poker4_s_tp():
    player_A = [('9', 'clubs'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('queen', 'diamonds'), ('queen', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Straight should win"

def test_poker5_s_hc():
    player_A = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('9', 'spades'), ('king', 'clubs'), ('queen', 'clubs'), ('5', 'clubs'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Straight should win"

def test_poker4_s_hc():
    player_A = [('9', 'clubs'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('9', 'spades'), ('king', 'clubs'), ('queen', 'clubs'), ('jack', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Straight should win"

def test_poker3_s_hc():
    player_A =[('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    player_B = [('9', 'spades'), ('king', 'clubs'), ('queen', 'clubs')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Straight should win"

def test_poker5_tk_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    player_B = [('queen', 'diamonds'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Royal Flush should win"

def test_poker4_tk_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('queen', 'diamonds'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should win"

def test_poker3_tk_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')]
    player_B = [('queen', 'diamonds'), ('queen', 'spades'), ('queen', 'clubs')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Royal Flush should win"

def test_poker5_tk_fh():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'spades'), ('king', 'diamonds')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Full House should win"

def test_poker5_tk_f():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Flush should win"

def test_poker4_tk_f():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Flush should win"

def test_poker3_tk_f():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Flush should win"

def test_poker5_tk_s():
    player_A = [('queen', 'hearts'), ('queen', 'diamonds'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'clubs'), ('10', 'hearts')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Straight should win"

def test_poker4_tk_s():
    player_A = [('queen', 'hearts'), ('queen', 'diamonds'), ('queen', 'clubs'), ('jack', 'spades')]
    player_B = [('king', 'diamonds'), ('queen', 'spades'), ('jack', 'clubs'), ('10', 'hearts')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Straight should win"

def test_poker3_tk_s():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs')]
    player_B = [('king', 'diamonds'), ('queen', 'diamonds'), ('jack', 'clubs')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Straight should win"

def test_poker5_tk_tk_A():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('8', 'hearts'), ('8', 'spades'), ('8', 'clubs'), ('jack', 'clubs'), ('10', 'clubs')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"3 of a kind A should win"

def test_poker4_tk_tk_A():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades')]
    player_B = [('8', 'hearts'), ('8', 'spades'), ('8', 'clubs'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"3 of a kind A should win"

def test_poker4_tk_tk_B():
    player_B = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades')]
    player_A = [('8', 'hearts'), ('8', 'spades'), ('8', 'clubs'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"3 of a kind B should win"

def test_poker3_tk_tk_A():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs')]
    player_B = [('8', 'hearts'), ('8', 'spades'), ('8', 'clubs')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"3 of a kind A should win"

def test_poker3_tk_tk_B():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('king', 'clubs')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"3 of a kind B should win"

def test_poker5_tk_tp():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('jack', 'diamonds'), ('jack', 'hearts'), ('10', 'clubs')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"3 of a kind should win"

def test_poker4_tk_tp():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('jack', 'diamonds'), ('jack', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"3 of a kind should win"

def test_poker3_tk_op():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs')]
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"3 of a kind should win"

def test_poker5_tk_hc():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('9', 'spades'), ('king', 'diamonds'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'hearts')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"3 of a kind should win"

def test_poker5_tp_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    player_B = [('king', 'diamonds'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'clubs'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Royal Flush should win"

def test_poker4_tp_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('king', 'diamonds'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should win"

def test_poker5_tp_sf():
    player_A = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('king', 'diamonds'), ('king', 'spades'), ('queen', 'diamonds'), ('queen', 'clubs'), ('10', 'clubs')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Straight flush should win"

def test_poker4_tp_sf():
    player_A = [('10', 'spades'), ('9', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
    player_B = [('king', 'diamonds'), ('king', 'spades'), ('queen', 'diamonds'), ('queen', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Straight flush should win"

def test_poker5_tp_f():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    player_B = [('king', 'diamonds'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'clubs'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Flush should win"

def test_poker4_tp_f():
    player_A = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades')]
    player_B = [('king', 'diamonds'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Flush should win"

def test_poker4_tp_s():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('king', 'diamonds'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Straight should win"

def test_poker5_tp_tk():
    player_A = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    player_B = [('king', 'diamonds'), ('king', 'spades'), ('10', 'clubs'), ('queen', 'diamonds'), ('10', 'hearts')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"3 of a kind should win"

def test_poker4_tp_tk():
    player_A = [('ace', 'hearts'), ('ace', 'spades'), ('10', 'hearts'), ('10', 'spades')]
    player_B = [('king', 'diamonds'), ('king', 'spades'), ('king', 'clubs'), ('queen', 'diamonds')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"3 of a kind should win"

def test_poker5_tp_tp_A():
    player_B = [('jack', 'diamonds'), ('jack', 'spades'), ('queen', 'diamonds'), ('queen', 'clubs'), ('10', 'hearts')]
    player_A = [('king', 'hearts'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"2 pair A should win"

def test_poker5_tp_tp_B():
    player_A = [('jack', 'diamonds'), ('jack', 'spades'), ('queen', 'diamonds'), ('queen', 'clubs'), ('10', 'hearts')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"2 pair B should win"

def test_poker5_tp_tp():
    player_A = [('king', 'diamonds'), ('king', 'clubs'), ('queen', 'diamonds'), ('queen', 'clubs'), ('10', 'hearts')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    assert "Draw" in session6.poker_2_player(5, [player_A,player_B]),"2 pair should be draw"

def test_poker4_tp_tp_A():
    player_B = [('jack', 'diamonds'), ('jack', 'spades'), ('queen', 'diamonds'), ('queen', 'clubs')]
    player_A = [('king', 'hearts'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"2 pair A should win"

def test_poker4_tp_tp_B():
    player_A = [('jack', 'diamonds'), ('jack', 'spades'), ('queen', 'diamonds'), ('queen', 'clubs')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'hearts')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"2 pair B should win"

def test_poker4_tp_tp():
    player_A = [('king', 'diamonds'), ('king', 'clubs'), ('queen', 'diamonds'), ('queen', 'clubs')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'hearts')]
    assert "Draw" in session6.poker_2_player(4, [player_A,player_B]),"2 pair should be draw"

def test_poker5_tp_op():
    player_A = [('king', 'diamonds'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'clubs'), ('10', 'clubs')]
    player_B = [('king', 'clubs'), ('king', 'hearts'), ('jack', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"2 Pair should win"

def test_poker4_tp_op():
    player_A = [('king', 'diamonds'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'clubs')]
    player_B = [('king', 'clubs'), ('king', 'hearts'), ('jack', 'spades'), ('queen', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"2 Pair should win"

def test_poker5_tp_hc():
    player_A =[('king', 'diamonds'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'clubs'), ('10', 'spades')]
    player_B = [('9', 'spades'), ('king', 'hearts'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'hearts')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"2 Pair should win"

def test_poker5_op_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'clubs'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"Royal Flush should win"

def test_poker4_op_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should win"

def test_poker3_op_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')]
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Royal Flush should win"

def test_poker5_op_sf():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'clubs'), ('queen', 'hearts'), ('10', 'clubs')]
    player_B = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Straight flush should win"

def test_poker4_op_sf():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'clubs'), ('queen', 'hearts')]
    player_B = [('10', 'spades'), ('9', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Straight flush should win"

def test_poker3_op_sf():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'clubs')]
    player_B = [('jack', 'spades'), ('10', 'spades'), ('queen', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Straight flush should win"

def test_poker5_op_fh():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    player_B = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'hearts'), ('king', 'diamonds')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Full House should win"

def test_poker5_op_f():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('7', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Flush should win"

def test_poker4_op_f():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'hearts')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Flush should win"

def test_poker3_op_f():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades')]
    player_B = [('9', 'spades'), ('2', 'spades'), ('3', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Flush should win"

def test_poker5_op_s():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'clubs'), ('queen', 'hearts'), ('10', 'spades')]
    player_B = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Straight should win"

def test_poker4_op_s():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'clubs'), ('queen', 'hearts')]
    player_B = [('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Straight should win"

def test_poker3_op_s():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'clubs')]
    player_B = [('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Straight should win"

def test_poker3_op_tk():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'diamonds')]
    player_B = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"3 of a kind should win"

def test_poker4_op_tp():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'clubs')]
    player_B = [('king', 'hearts'), ('king', 'diamonds'), ('queen', 'spades'), ('queen', 'hearts')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"2 pair should win"

def test_poker4_op_op_A():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'hearts')]
    player_B = [('queen', 'clubs'), ('queen', 'spades'), ('10', 'spades'), ('9', 'hearts')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"1 pair A should win"

def test_poker4_op_op_B():
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'hearts')]
    player_A = [('queen', 'clubs'), ('queen', 'spades'), ('10', 'spades'), ('9', 'hearts')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"1 Pair B should win"

def test_poker3_op_op_A():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades')]
    player_B = [('queen', 'clubs'), ('queen', 'spades'), ('10', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"1 Pair A should win"

def test_poker3_op_op_B():
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades')]
    player_A = [('queen', 'clubs'), ('queen', 'spades'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"1 Pair B should win"

def test_poker3_op_op():
    player_A = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades')]
    player_B = [('king', 'hearts'), ('king', 'diamonds'), ('jack', 'clubs')]
    assert "Draw" in session6.poker_2_player(3, [player_A,player_B]),"1 Pair should be a draw"

def test_poker4_op_hc():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('9', 'spades'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"1 Pair should win"

def test_poker3_op_hc():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')]
    player_B = [('9', 'spades'), ('king', 'diamonds'), ('queen', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"1 Pair should win"

def test_poker5_hc_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    player_B =[('9', 'spades'), ('king', 'diamonds'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B])," Royal Flush should  win"

def test_poker4_hc_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts')]
    player_B = [('9', 'spades'), ('king', 'diamonds'), ('5', 'spades'), ('jack', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"Royal Flush should  win"

def test_poker3_hc_rf():
    player_A = [('ace', 'hearts'), ('king', 'hearts'), ('queen', 'hearts')]
    player_B = [('9', 'spades'), ('king', 'diamonds'), ('5', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"Royal Flush should  win"

def test_poker3_hc_sf():
    player_A =[('9', 'spades'), ('king', 'diamonds'), ('5', 'spades')]
    player_B = [('jack', 'spades'), ('10', 'spades'), ('queen', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"Straight flush should win"

def test_poker5_hc_fh():
    player_A = [('9', 'spades'), ('king', 'hearts'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'hearts')]
    player_B = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'), ('king', 'spades'), ('king', 'diamonds')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Full House should win"

def test_poker5_hc_s():
    player_A =[('9', 'spades'), ('king', 'hearts'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    player_B = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"Straight should win"

def test_poker4_hc_s():
    player_A = [('9', 'spades'), ('king', 'hearts'), ('5', 'spades'), ('jack', 'clubs')]
    player_B = [('king', 'diamonds'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'hearts')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"Straight should win"

def test_poker5_hc_tk():
    player_A = [('9', 'spades'), ('king', 'diamonds'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'hearts')]
    player_B = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"3 of a kind should win"

def test_poker4_hc_tk():
    player_A =[('9', 'spades'), ('king', 'diamonds'), ('5', 'spades'), ('jack', 'clubs')]
    player_B = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"3 of a kind should win"

def test_poker3_hc_tk():
    player_A =[('9', 'spades'), ('king', 'diamonds'), ('5', 'spades')]
    player_B = [('queen', 'hearts'), ('queen', 'spades'), ('queen', 'clubs')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"3 of a kindh should win"

def test_poker5_hc_tp():
    player_A =[('9', 'spades'), ('king', 'diamonds'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'hearts')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"2 pair should win"

def test_poker4_hc_tp():
    player_A =[('9', 'spades'), ('king', 'diamonds'), ('5', 'spades'), ('jack', 'clubs')]
    player_B = [('king', 'hearts'), ('king', 'spades'), ('queen', 'spades'), ('queen', 'hearts')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"2 pair should win"

def test_poker5_hc_op():
    player_A = [('9', 'spades'), ('king', 'diamonds'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'hearts')]
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'clubs'), ('10', 'spades')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"1 pair should win"

def test_poker4_hc_op():
    player_A = [('9', 'spades'), ('king', 'diamonds'), ('5', 'spades'), ('jack', 'clubs')]
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades'), ('queen', 'clubs')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"1 pair should win"

def test_poker3_hc_op():
    player_A =[('9', 'spades'), ('king', 'diamonds'), ('5', 'spades')]
    player_B = [('king', 'clubs'), ('king', 'spades'), ('jack', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"1 pair should win"

def test_poker5_hc_hc_A():
    player_A = [('9', 'clubs'), ('king', 'diamonds'), ('5', 'hearts'), ('jack', 'diamonds'), ('10', 'hearts')]
    player_B = [('9', 'spades'), ('queen', 'diamonds'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert "Player A" in session6.poker_2_player(5, [player_A,player_B]),"High Card A should win"

def test_poker5_hc_hc_B():
    player_B = [('9', 'clubs'), ('king', 'diamonds'), ('5', 'hearts'), ('jack', 'diamonds'), ('10', 'hearts')]
    player_A = [('9', 'spades'), ('queen', 'diamonds'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert "Player B" in session6.poker_2_player(5, [player_A,player_B]),"High Card B should win"

def test_poker5_hc_hc():
    player_A = [('9', 'clubs'), ('king', 'diamonds'), ('5', 'hearts'), ('jack', 'diamonds'), ('10', 'hearts')]
    player_B = [('9', 'spades'), ('king', 'hearts'), ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert "Draw" in session6.poker_2_player(5, [player_A,player_B]),"High Card should be a draw"

def test_poker4_hc_hc_A():
    player_A = [('9', 'clubs'), ('king', 'diamonds'), ('5', 'hearts'), ('jack', 'diamonds')]
    player_B = [('9', 'spades'), ('queen', 'diamonds'), ('5', 'spades'), ('jack', 'clubs')]
    assert "Player A" in session6.poker_2_player(4, [player_A,player_B]),"High Card A should win"

def test_poker4_hc_hc_B():
    player_B = [('9', 'clubs'), ('king', 'diamonds'), ('5', 'hearts'), ('jack', 'diamonds')]
    player_A = [('9', 'spades'), ('queen', 'diamonds'), ('5', 'spades'), ('jack', 'clubs')]
    assert "Player B" in session6.poker_2_player(4, [player_A,player_B]),"High Card B should win"

def test_poker4_hc_hc():
    player_A = [('9', 'clubs'), ('king', 'diamonds'), ('5', 'hearts'), ('jack', 'diamonds')]
    player_B = [('9', 'spades'), ('king', 'hearts'), ('5', 'spades'), ('jack', 'clubs')]
    assert "Draw" in session6.poker_2_player(4, [player_A,player_B]),"High Card should be a draw"

def test_poker3_hc_hc_A():
    player_A = [('ace', 'hearts'), ('jack', 'clubs'), ('queen', 'hearts')]
    player_B = [('9', 'spades'), ('jack', 'diamonds'), ('queen', 'spades')]
    assert "Player A" in session6.poker_2_player(3, [player_A,player_B]),"High Card A should win"

def test_poker3_hc_hc_B():
    player_B = [('ace', 'hearts'), ('jack', 'clubs'), ('queen', 'hearts')]
    player_A = [('9', 'spades'), ('jack', 'diamonds'), ('queen', 'spades')]
    assert "Player B" in session6.poker_2_player(3, [player_A,player_B]),"High Card B should win"

def test_poker3_hc_hc():
    player_A = [('ace', 'hearts'), ('jack', 'clubs'), ('queen', 'hearts')]
    player_B = [('jack', 'spades'), ('ace', 'diamonds'), ('queen', 'spades')]
    assert "Draw" in session6.poker_2_player(3, [player_A,player_B]),"High Card should be a draw"

def test_doc_deck_lmz():
    assert bool(session6.deck_generator_lmz.__doc__), "No DocString - deck_generator_lmz"

def test_ann_deck_lmz():
    assert bool(session6.deck_generator_lmz.__annotations__), "No Annotations - deck_generator_lmz"

def test_doc_deck():
    assert bool(session6.deck_generator.__doc__), "No DocString - deck_generator"

def test_ann_deck():
    assert bool(session6.deck_generator.__annotations__), "No Annotations - deck_generator"

def test_doc_dealer():
    assert bool(session6.card_dealer.__doc__), "No DocString - card_dealer"

def test_ann_dealer():
    assert bool(session6.card_dealer.__annotations__), "No Annotations - card_dealer"

def test_doc_royal_flush():
    assert bool(session6.royalflush.__doc__), "No DocString - royalflush"

def test_ann_royal_flush():
    assert bool(session6.royalflush.__annotations__), "No Annotations - royalflush"

def test_doc_straight_flush():
    assert bool(session6.straightflush.__doc__), "No DocString - straightflush"

def test_ann_straight_flush():
    assert bool(session6.straightflush.__annotations__), "No Annotations - straightflush"

def test_doc_four_kind():
    assert bool(session6.fourofakind.__doc__), "No DocString - fourofakind"

def test_ann_four_kind():
    assert bool(session6.fourofakind.__annotations__), "No Annotations - fourofakind"

def test_doc_full_house():
    assert bool(session6.fullhouse.__doc__), "No DocString - fullhouse"

def test_ann_full_house():
    assert bool(session6.fullhouse.__annotations__), "No Annotations - fullhouse"

def test_doc_flush():
    assert bool(session6.flush.__doc__), "No DocString - flush"

def test_ann_flush():
    assert bool(session6.flush.__annotations__), "No Annotations - flush"

def test_doc_straight():
    assert bool(session6.straight.__doc__), "No DocString - straight"

def test_ann_straight():
    assert bool(session6.straight.__annotations__), "No Annotations - straight"

def test_doc_three_kind():
    assert bool(session6.threeofakind.__doc__), "No DocString - threeofakind"

def test_ann_three_kind():
    assert bool(session6.threeofakind.__annotations__), "No Annotations - threeofakind"

def test_doc_two_pair():
    assert bool(session6.twopair.__doc__), "No DocString - twopair"

def test_ann_two_pair():
    assert bool(session6.twopair.__annotations__), "No Annotations - twopair"

def test_doc_one_pair():
    assert bool(session6.onepair.__doc__), "No DocString - onepair"

def test_ann_one_pair():
    assert bool(session6.onepair.__annotations__), "No Annotations - onepair"

def test_doc_highcard():
    assert bool(session6.highcard.__doc__), "No DocString - highcard"

def test_ann_highcard():
    assert bool(session6.highcard.__annotations__), "No Annotations - highcard"

def test_doc_rank():
    assert bool(session6.rank.__doc__), "No DocString - rank"

def test_ann_rank():
    assert bool(session6.rank.__annotations__), "No Annotations - rank"

def test_doc_poker_2_player():
    assert bool(session6.poker_2_player.__doc__), "No DocString - poker_2_player"

def test_ann_poker_2_player():
    assert bool(session6.poker_2_player.__annotations__), "No Annotations - poker_2_player"
