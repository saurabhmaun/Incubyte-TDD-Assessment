# string_calculator.py

import re

def add(numbers):
    if numbers == '': return 0

    numbers = map(int, re.findall(r"-?\d+", numbers))
    numbers = filter(lambda x: x < 1000, numbers)
    
    # return the sum
    return sum(numbers)