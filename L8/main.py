def hpwmanyletters(input: str):
    if len(input) < 1:
        return "no data"
    elif len(input) < 3:
        return "less three letters!"

    return str(input).split(" ")