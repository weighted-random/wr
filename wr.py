import random
from collections import Mapping

def choice(data):
    if isinstance(data, Mapping):
        dataitems = data.items()
        totalweights = sum(data.values()) - 1
    else:
        dataitems = data
        totalweights = sum([i[1] for i in data]) - 1
    
    randomindex = random.randint(0, totalweights)
    count = 0
    for returnable, weight in dataitems:
            count += weight
            if count > randomindex:
                    return returnable

