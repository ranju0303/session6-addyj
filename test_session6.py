import pytest
import re
import inspect
import os
import session6
import test_session6

README_CONTENT_CHECK_FOR = [
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
        'rank',
        'poker_2_player'
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
    readme = open("README.md", "r")
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

def test_poker_2_player():
    for i in range(200):
        card_count, deal = session6.card_dealer(suits, cards)
        assert "Player" in session6.poker_2_player(card_count, deal), 'your poker game fails somewhere...'

    #
    #
    # 'deck_generator_lmz',
    # 'deck_generator',
    # 'card_dealer',
    # 'royalflush',
    # 'straightflush',
    # 'fourofakind',
    # 'fullhouse',
    # 'flush',
    # 'straight',
    # 'threeofakind',
    # 'twopair',
    # 'onepair',
    # 'highcard',
    # 'rank',
    # 'poker_2_player',
    # 'ValueError'

# for i in range(200000):
#


## test case
# def handy(cards='2♥ 2♦ 2♣ k♣ q♦'):
#     hand = []
#     for card in cards.split():
#         f, s = card[:-1], card[-1]
#         assert f in face, "Invalid: Don't understand card face %r" % f
#         assert s in suit, "Invalid: Don't understand card suit %r" % s
#         hand.append(Card(f, s))
#     assert len(hand) == 5, "Invalid: Must be 5 cards in a hand, not %i" % len(hand)
#     assert len(set(hand)) == 5, "Invalid: All cards in the hand must be unique %r" % cards
#     return hand

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
