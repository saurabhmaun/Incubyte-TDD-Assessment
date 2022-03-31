# string_calculator.py

import re


def check_negetive_numbers(str1):
    # filter negetive numbers and raise exception
    negative_numbers = list(filter(lambda x: x < 0, str1))
    if negative_numbers: raise Exception('negatives not allowed ' + str(negative_numbers))

def add(numbers):
    if numbers == '': return 0

    numbers = map(int, re.findall(r"-?\d+", numbers))
    numbers = list(filter(lambda x: x < 1000, numbers))

    check_negetive_numbers(numbers)

    # return the sum
    return sum(numbers)


# sum of odd index
# sum of even index
# output : even - odd
def new_add(numbers):
    if numbers == '': return 0
    numbers = map(int, re.findall(r"-?\d+", numbers))
    numbers = list(filter(lambda x: x < 1000, numbers))
    
    check_negetive_numbers(numbers)

    odd_index_sum = 0
    even_index_sum = 0
    for idx, x in enumerate(numbers):
        if idx % 2 == 0:
            even_index_sum = even_index_sum + x
        else:
            odd_index_sum = odd_index_sum + x

    return (even_index_sum - odd_index_sum)