def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost

    """

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
   


def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot 
    
    """

    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    

def lose(power_pellet_active, touching_ghost):
    return not power_pellet_active and touching_ghost
    
    """

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)

    """

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
   
print("El jugador puede comer el fantasma?")
print(eat_ghost(True, False))

print("El jugador consigue un punto?")
print(score(True, False))

print("El jugador perdio?")
print(lose(False, False))

print("El jugador gano?")
print(win(True, True, True))