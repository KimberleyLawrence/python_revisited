def distance_from_zero(argument):
    if type(argument) == int or type(argument) == float:
        return abs(argument)
    else:
        return "Nope"
