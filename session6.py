import random

# ordered tuples of cards
rank_card_list = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace')
low_ace_rank_card_list = ('ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king')

def deck_generator_lmz(suits:'suits type set', cards:'cards type set') -> 'returns all valid possible cards in deck':
    # generator function for a card in deck
    ''' This function generates all possible valid playing cards of a deck
    using only lambda, zip, and map inbuilt functions.
    '''
    deck_full = set(zip(list(map(lambda x : x , cards))*4, list(map(lambda x : x , suits))*13))
    return deck_full

def deck_generator(suits:'suits type set', cards:'cards type set') -> 'returns all valid possible cards in deck':
    # generator function for a card in deck
    ''' This function generates all possible valid playing cards of a deck.'''
    deck_cards = set()
    for card in cards:
        for suit in suits:
            deck_cards.add((card, suit))
    return deck_cards

def card_dealer(suits:'suits type set', cards:'cards type set') -> 'tuple':
    '''
    Function generates a 52 unique card for a deck.
    Dealt each player a hand of 3/4/5 cards.
    return card count and list of hands of all players as tuple.
    '''
    card_number = random.choice([3, 4, 5])
    deck_full = deck_generator(suits, cards)
    player_one = set(random.sample(deck_full, card_number))
    left_deck_deal = deck_full - player_one
    player_two = set(random.sample(left_deck_deal, card_number))
    return card_number, [player_one, player_two]

def royalflush(hand: 'poker hand to check for') -> 'tuple':
    '''
    Function takes a poker hand and determine if its a royal flush hand and its tiebreaker card
    returns False if not royal flush
    else returns a tuple of type and tie card.
    '''
    royal_rank_string = ' '.join([cr for cr in rank_card_list[-5:]])
    ordered = sorted(hand, key=lambda x : (rank_card_list.index(x[0]), x[1]))
    first, rest = ordered[0], ordered[1:]
    if all(suit == first[1] for card, suit in rest):
        if ' '.join(card for card, suit in ordered) in royal_rank_string:
            return 'royal_flush', ordered[-1][0]
    return False

def straightflush(hand: 'poker hand to check for') -> 'tuple':
    '''
    Function takes a poker hand and determine if its a straight flush hand and its tiebreaker card
    returns False if not straight flush
    else returns a tuple of type and tie card.
    '''
    if any(card == '2' for card, suit in hand):
        card_rank = low_ace_rank_card_list
    else:
        card_rank = rank_card_list

    ordered = sorted(hand, key=lambda x: (card_rank.index(x[0]), x[1]))
    first, rest = ordered[0], ordered[1:]
    card_rank_string = ' '.join([cr for cr in card_rank])
    if (all(suit == first[1] for card, suit in rest) and
    ' '.join(card for card, suit in ordered) in card_rank_string):
        return 'straight_flush', ordered[-1][0]
    return False

def fourofakind(hand: 'poker hand to check for') -> 'tuple':
    '''
    Function takes a poker hand and determine if its a four of a kind hand and its tiebreaker list
    returns False if not four of a kind
    else returns a tuple of type and tie list.
    '''
    allcards = [card for card, suit in hand]
    allcardtypes = set(allcards)
    if(len(hand) == 5):
        if len(allcardtypes) != 2:
            return False
    elif(len(hand) == 4):
        if len(allcardtypes) != 1:
            return False
    for card in allcardtypes:
        if allcards.count(card) == 4:
            allcardtypes.remove(card)
            if allcardtypes:
                last_card = allcardtypes.pop()
                return 'four_of_a_kind', [card, last_card]
            else:
                return 'four_of_a_kind', [card]
    else:
        return False

def fullhouse(hand: 'poker hand to check for') -> 'tuple':
    '''
    Function takes a poker hand and determine if its a full house hand and its tiebreaker list
    returns False if not full house
    else returns a tuple of type and tie list.
    '''
    allcards = [card for card, suit in hand]
    allcardtypes = set(allcards)
    if len(allcardtypes) != 2:
        return False
    for card in allcardtypes:
        if allcards.count(card) == 3:
            allcardtypes.remove(card)
            if allcardtypes:
                last_card = allcardtypes.pop()
                return 'full_house', [card, last_card]
            else:
                return 'full_house', [card]
    else:
        return False

def flush(hand: 'poker hand to check for') -> 'tuple':
    '''
    Function takes a poker hand and determine if its a flush hand and its tiebreaker list
    returns False if not flush
    else returns a tuple of type and tie list.
    '''
    allsuittypes = {suit for card, suit in hand}
    if len(allsuittypes) == 1:
        allcards = [card for card, suit in hand]
        return 'flush', sorted(allcards,
                                key=lambda card: rank_card_list.index(card),
                                reverse=True)
    return False

def straight(hand: 'poker hand to check for') -> 'tuple':
    '''
    Function takes a poker hand and determine if its a straight hand and its tiebreaker card
    returns False if not straight
    else returns a tuple of type and tie card.
    '''
    if any(card == '2' for card, suit in hand):
        card_rank = low_ace_rank_card_list
    else:
        card_rank = rank_card_list
    ordered = sorted(hand, key=lambda x: (card_rank.index(x[0]), x[1]))
    first, rest = ordered[0], ordered[1:]
    card_rank_string = ' '.join([cr for cr in card_rank])
    if ' '.join(card for card, suit in ordered) in card_rank_string:
        return 'straight', ordered[-1][0]
    return False

def threeofakind(hand: 'poker hand to check for') -> 'tuple':
    '''
    Function takes a poker hand and determine if its a three of a kind hand and its tiebreaker list
    returns False if not three of a kind
    else returns a tuple of type and tie list.
    '''
    allcards = [card for card, suit in hand]
    allcardtypes = set(allcards)
    if(len(hand) == 5):
        if len(allcardtypes) <= 2:
            return False
    elif(len(hand) == 4):
        if len(allcardtypes) <= 1:
            return False
    elif(len(hand) == 3):
        if len(allcardtypes) <= 0:
            return False
    for card in allcardtypes:
        if allcards.count(card) == 3:
            allcardtypes.remove(card)
            return ('three_of_a_kind', [card] +
                        sorted(allcardtypes,
                                key=lambda card: rank_card_list.index(card),
                                reverse=True))
    else:
        return False

def twopair(hand: 'poker hand to check for') -> 'tuple':
    '''
    Function takes a poker hand and determine if its a two pair hand and its tiebreaker list
    returns False if not two pair
    else returns a tuple of type and tie list.
    '''
    allcards = [card for card, suit in hand]
    allcardtypes = set(allcards)
    pairs = [card for card in allcardtypes if allcards.count(card) == 2]
    if len(pairs) != 2:
        return False
    p0, p1 = pairs
    remaining_card_type = allcardtypes - set(pairs)
    other = [remaining_card_type.pop()] if remaining_card_type else []
    return 'two_pair', pairs + other if rank_card_list.index(p0) > rank_card_list.index(p1) else pairs[::-1] + other

def onepair(hand: 'poker hand to check for') -> 'tuple':
    '''
    Function takes a poker hand and determine if its a one pair hand and its tiebreaker list
    returns False if not one pair
    else returns a tuple of type and tie list.
    '''
    allcards = [card for card, suit in hand]
    allcardtypes = set(allcards)
    pairs = [card for card in allcardtypes if allcards.count(card) == 2]
    if len(pairs) != 1:
        return False
    allcardtypes.remove(pairs[0])
    return 'one_pair', pairs + sorted(allcardtypes,
                                        key=lambda card: rank_card_list.index(card),
                                        reverse=True)

def highcard(hand: 'poker hand to check for') -> 'tuple':
    '''
    Function takes a poker hand and determine the high card and the tiebreaker list
    returns a tuple of type and tie list.
    '''
    allcards = [card for card, suit in hand]
    return 'high_card', sorted(allcards,
                                key=lambda card: rank_card_list.index(card),
                                reverse=True)

def rank(rank_order: 'rank order list', hand: 'hand of player') -> 'tuple':
    '''
    Determine the type of hand from the rank order list provided which is
    based on the possibilities for a given card count.
    returns a tuple of type and tie list for that hand.
    '''
    for ranker in rank_order:
        rank = ranker(hand)
        if rank:
            break
    if not rank:
        raise ValueError(f'Invalid: Failed to rank cards: {hand}')
    return rank

def poker_2_player(card_count : 'number of cards per player', deal: 'poker hands of each player') -> 'the winning player':
    '''
    Poker Game for 2 players with single deck of cards.
    The function takes in the cards count which are distributed/dealt to
    each player and the eacxt cards of the players.
    Based on the poker rules mentioned in README it decides which player has won.
    As the game has 3/4/5 cards in a hand per player per game the rank possibilities differ based on that.
    3 card : ['royal_flush', 'straight_flush', 'flush', 'straight', 'three_of_a_kind', 'one_pair', 'high_card']
    4 card : ['royal_flush', 'straight_flush', 'four_of_a_kind', 'flush', 'straight', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']
    5 card : ['royal_flush', 'straight_flush', 'four_of_a_kind', 'full_house', 'flush', 'straight', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']
    '''
    win_order = ['royal_flush', 'straight_flush', 'four_of_a_kind', 'full_house', 'flush', 'straight', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']

    if not isinstance(card_count, int) and not isinstance(deal, list):
        raise ValueError("dealer is shitty...wrong datatypes...")
    if not len(deal) == 2:
        raise ValueError("Numbers of players are not according to the rules...")
    if card_count < 3:
        raise ValueError("Cards dealt are innsufficient...")
    if card_count > 5:
        raise ValueError("Boss not playing poker i guess...")

    if card_count == 3:
        handrankorder = (royalflush, straightflush, flush, straight,
                        threeofakind, onepair, highcard)
    elif card_count == 4:
        handrankorder = (royalflush, straightflush, fourofakind, flush,
                        straight, threeofakind, twopair, onepair, highcard)
    elif card_count == 5:
        handrankorder = (royalflush, straightflush, fourofakind, fullhouse,
                        flush, straight, threeofakind, twopair, onepair,
                        highcard)
    player_card_type = []
    for player_hand in deal:
        player_card_type.append(rank(handrankorder, list(player_hand)))
    if win_order.index(player_card_type[0][0]) < win_order.index(player_card_type[1][0]):
        return f'YAY... Player A wins!!! by {player_card_type[0][0]}'
    elif win_order.index(player_card_type[0][0]) > win_order.index(player_card_type[1][0]):
        return f'YAY... Player B wins!!! by {player_card_type[1][0]}'
    elif win_order.index(player_card_type[0][0]) == win_order.index(player_card_type[1][0]):
        return f'Draw Match between Player A and B by {player_card_type[0][0]} as not comparing rest of the cards...sorry...'
    else:
        return f'Draw Match between Player A and B by {player_card_type[0][0]}'
