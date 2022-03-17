# string_calculator.py

import re

def add(numbers):
    if numbers == '': return 0

    numbers = map(int, re.findall(r"-?\d+", numbers))
    numbers = list(filter(lambda x: x < 1000, numbers))

    # filter negetive numbers and raise exception
    negative_numbers = list(filter(lambda x: x < 0, numbers))
    if negative_numbers: raise Exception('negatives not allowed ' + str(negative_numbers))

    # return the sum
    return sum(numbers)