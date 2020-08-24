## Diving into the nooks and cranny of an awesome language - PYTHON

### EPAi Session 6

### Understanding First Class Functions

---

#### Run test cases from test .py file

`$ pytest -vv`

---

### We looked over :

- Default Values
- Docstrings & Annotations
- Lambda Expressions
- Functional Introspection
- Callables
- Map, Filter & Zip

---

**Poker Rules**

Hand Ranking Categories

In Poker, there are about 10 ranking categories from highest to lowest:
1. Royal Flush 
At the top of the pile is a set of five suited consecutive cards with an ace as its highest card. No other hand can beat it, and if two or more active players have it, the pot is split evenly among them. Example: As Ks Qs Js 10s
2. Straight Flush
It’s practically the same as a royal flush but it uses a king or lower as its highest card.
If two or more active players have it, the player with the highest high card wins. The pot gets split evenly between players with the same highest cards. Example: Qc Jc 10c 9c 8c
3. Four of a Kind
This poker hand is made up of four cards of the same value and a random fifth card to complete the set.
In case there’s a tie, the fifth kicker card is used to determine a winner. If the fifth card on the table is higher than the highest kicker card any active player is holding, however, the pot is split evenly among all tied players. Example: 2d 2h 2s 2c Kh
4. Full House
This hand consists of a set of three cards of the same value (also known as a trip) and another set of two cards of the same value (also known as a pair).
If there’s a tie, the trips are compared. If the trips are of the same value, then the pairs are compared. If they’re still tied, then the pot is split evenly among all tied players. Example: 7h 7s 7c 3d 3h
5. Flush
This hand is made up of any five suited cards.
To break ties, the highest high card of each player gets compared. If they’re the same, then the second highest card is checked. The process continues until either one player comes out on top or the pot gets split evenly among players holding flushes of the exact same value. Example: Qd 10d 7d 4d 2d
6. Straight
Five non-suited consecutive cards make up this hand.
Ties, in this case, are broken just like you would with flushes. Example: Jd 10c 9s 8h 7d
7. Three of a Kind
This hand is simply a trip plus two random cards.
In the event of a tie, the trip with the highest value wins. A fourth or fifth kicker card is used to determine a winner in case the trips are of the same value. Example: 5d 5h 5c Kd 9s
8. Two Pair
As the name implies, this hand is just a pair of pairs plus a random fifth card to complete the set.
The high pair is compared in case of a tie. If they’re of the same value, then the low pair is checked. If they’re still tied, then the fifth kicker card is used to determine a winner. Example: Kd Kh 7d 7s 3c
9. Pair
As you may have guessed, this hand only has one pair instead of two so it comes with three other random cards to complete the set.
Ties are broken by first comparing the pair and then moving on to the next three kicker cards in case the pairs are of the same value. Example: 9s 9c 6d 4s 2h
10. High Card
This hand is just five random cards.
Ties are broken in pretty much the same way as with flushes and straights. Example: 9h 6c 5s 3d 2d

**Disclaimer:** Have followed the normal poker rules. As we are comparing same count of cards, we can follow them , provided removing the hand possibilities which doesn't exists for hands with cards count less than5.

Also have NOT IMPLEMENTED the tie break logic.

#### Function Description

1. **deck_generator_lmz:** This function generates a valid deck of cards using lambda, zip, map inbuilt functions.
2. **deck_generator:** This function generates a valid deck of cards using normal for loop.
3. **card_dealer:** This function takes the possible suits and cards set and generates a valid poker hands for two players, with random card count of 3/4/5 for both.
4. **royalflush:** Checks is the player's hand is royal flush
5. **straightflush:** Checks is the player's hand is straight flush
6. **fourofakind:** Checks is the player's hand is four of a kind
7. **fullhouse:** Checks is the player's hand is full house
8. **flush:** Checks is the player's hand is flush
9. **straight:** Checks is the player's hand is straight
10. **threeofakind:** Checks is the player's hand is three of a kind
11. **twopair:** Checks is the player's hand is two pair
12. **onepair:** Checks is the player's hand is one pair
13. **highcard:** Checks is the player's hand is high card 
14. **rank:** Checks is the rank type of player's hand 
15. **poker_2_player:** 

---

#### Test Cases Description
[INCOMPLETE]
---

1. **test_readme_exists** : to assert if the code base consists a README file or not.
2. **test_readme_contents** : to assert if the README file is explained thoroughly with enough wordings.
3. **test_readme_proper_description** : to assert if README file is properly documented, i.e. all methods and function are explained.
4. **test_readme_file_for_formatting** : to assert if the README file is properly formatted with headings.
5. **test_indentations** : to assert if the code base is following PEP-8 code style formatting.
6. **test_function_name_had_cap_letter** : to assert if the method/function names doesn't contains capital letters as per PEP-8 style convention.
7. **test_function_count** : to assert if more than 25 test cases has been written in test file for qualean class.
8. **test_function_repeatations** : to assert if the test cases hasn't been repeated.

---