def random_names(randomizer, names):
    if len(names) == 0:
        return "No name provided"
    return randomizer.randomize(names)