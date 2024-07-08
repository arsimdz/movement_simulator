

import random


# defining the number of steps


# creating two array for containing x and y coordinate
# of size equals to the number of size and filled up with 0's
def random_walk(x, y):
    val = random.randint(1, 4)
    if val == 1:
        x = x + 1
    elif val == 2:
        x = x - 1

    elif val == 3:
        y = y + 1
    else:
        y = y - 1
    return x, y
