# string_calculator_test.py

import string_calculator
import pytest

def test_empty_string():
	# it should return 0 if the string is empty
	assert string_calculator.add('') == 0

def test_add_two_numbers():
    # it should test 2 numbers
	assert string_calculator.add('1, 2') == 3

def test_add_multiple_numbers():
	# it should test multiple numbers
    assert string_calculator.add('1, 2, 3') == 6