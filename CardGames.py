def get_rounds(number):
    
    rounds =[number, number+1, number+2]
    return rounds
    
    


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2
    


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    if number in rounds:
        return True
    return False
    


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)
     


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """
    if (hand[0] + hand[-1]) / 2 == card_average(hand) or hand[len(hand)//2] == card_average(hand):
        return True
    return False
    


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    if card_average(hand[::2]) == card_average(hand[1::2]):
        return True
    return False
    


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand

print("El numero de rondas siguientes a la actual")
print(get_rounds(10))

print("Sumar el total de dos barajas")
print(concatenate_rounds([10,20,12,11,2],[3,20,12,15,7]))

print("La carta esta dentro de la baraja?")
print(list_contains_round([10,20,12,11,2], 20))

print("El promedio de la baraja")
print(card_average([10,20,12,11,2]))

print("La mitad de la baraja es igual al promedio real?")
print(approx_average_is_average([10,10,12,11,2]))

print("Son iguales los entremedios?")
print(average_even_is_average_odd([10,10,12,11,2]))

print("Multiplicar la ultima carta de la baraja por 2 si es igual a 11")
print(maybe_double_last([10,6,12,5,11]))