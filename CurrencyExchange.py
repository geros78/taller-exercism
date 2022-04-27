from traceback import print_tb


def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return float(budget / exchange_rate)
    


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return float (budget - exchanging_value)
   


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return int(denomination * number_of_bills)
    


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return budget // denomination
    


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    actual_rate = (exchange_rate * (1 + spread/100))
    ex_mo = exchange_money(budget, actual_rate)
    return get_number_of_bills(ex_mo, denomination) * denomination
    


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    actual_rate = (exchange_rate * (1 + spread/100))
    ex_mo = exchange_money(budget, actual_rate)
    return int(ex_mo % denomination)


print("Cuanto es el valor del cambio?")
print(exchange_money(127.5, 1.2))

print("Cuanto es la cantidad que quedo del presupuesto?")
print(get_change(127.5, 120))

print("Cuanto es el valor todal del cambio de dinero?")
print(get_value_of_bills(5, 128))

print("Cuanto es la cantidad recibida segun la moneda de nueva circulacion?")
print(get_number_of_bills(127.5, 5))

print("Cuanto es el valor máximo de la nueva moneda después de calcular el tipo de cambio más el margen?")
print(exchangeable_value(127.25, 1.20, 10, 20))

print("Cuanto es el valor que no es canjeable debido a la denominación de los billetes?")
print(non_exchangeable_value(127.25, 1.20, 10, 5))