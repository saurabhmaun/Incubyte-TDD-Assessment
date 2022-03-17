# string_calculator_test.py

import string_calculator
import pytest

def test_empty_string():
	# it should return 0 if the string is empty
    print("Testing empty string")
    assert string_calculator.add('') == 0

def test_add_two_numbers():
    # it should test 2 numbers
    print("Testing 2 numbers in string")
    assert string_calculator.add('1, 2') == 3

def test_add_multiple_numbers():
	# it should test multiple numbers
    print("Testing multiple numbers in string")
    assert string_calculator.add('1, 2, 3') == 6

def test_add_new_line_character():
	# it should test new line character in number string
    print("Testing new line character in string")
    assert string_calculator.add('1\n2,3') == 6

def test_add_diff_delimeters():
	# it should test different delimeters in string
    print("Testing different delimeters in string")
    assert string_calculator.add("//;\n1;2") == 3

test_empty_string()
test_add_two_numbers()
test_add_multiple_numbers()
test_add_new_line_character()
test_add_diff_delimeters()