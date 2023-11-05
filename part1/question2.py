################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function
# should change (x, y) into (y, x).
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in
# `question2_test.py.`


# We can use a lambda expression to swap the items of the tuple.
swapper = (lambda x: (x[1], x[0]))


def run_swapper(list_of_tuples):
    """
    Swap the order of elements in a tuple.

    Keyword arguments:
    list_of_tuples -- list of tuples to which you want to exchange the positions of your items.
    """
    return list(map(swapper, list_of_tuples))
