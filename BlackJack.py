def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    cards = ['J','Q','K']
    
    if card in cards:
        return 10
    if card == 'A':
        return 1
    return int(card)




def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    else:
        return card_two



def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.

    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    if value_of_card(card_one)== 1 or value_of_card(card_two)== 1:
        return 1
    
    ace_chose = (value_of_card(card_one) + value_of_card(card_two))+ 11

    if ace_chose > 21:
        return 1
    else:
        return 11
    

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    cards = ['J', 'Q', 'K', '10']
    
    if (card_one == 'A' and card_two in cards) or (card_two == 'A' and card_one in cards):
        return True
    else:
        return False
    

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)



def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    double_down = [9, 10, 11]
    return value_of_card(card_one) + value_of_card(card_two) in double_down


print("Valor de la carta:")
print(value_of_card('A'))

print("Cual carta es mayor?")
print(higher_card(8,9))

print("La carta mas ventajosa segun el valor de la mano:")
print(value_of_ace(2,2))

print("Es blackjack?")
print(is_blackjack('A','J'))

print("Pudes repartir la baraja de carta en partes?")
print(can_split_pairs(2,2))

print("Puedes hacer una apuesta doble?")
print(can_double_down(5, 4))
