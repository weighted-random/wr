from itertools import islice
from random import randint

def wr(data):
    """ Returns a key of the passed in dict.
        model: (key, weight)
        example: get_wrr({'cat': 80, 'dog': 20})
    """

    def build_population(data):
        """ Builds a sample population of the data.
        """
        for item, weight in data.items():
            for _ in range(weight):
                yield item

    population = build_population(data)
    populationsize = sum(data.values())
    index = randint(0, populationsize - 1)
    return islice(population, index, None).next()

# Alias
get = wr
