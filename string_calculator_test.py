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

def test_negative_numbers():
	# it should raise an exception containing all negative numbers if any are found
    print("Testing negetive numbers in string")
    with pytest.raises(Exception, match = r'negatives not allowed \[-1, -2, -3\]'):
        string_calculator.add('-1, -2, -3, 1, 2, 3')

# Code Extension
def test_empty_string():
	# it should return 0 if the string is empty
    print("Testing empty string")
    assert string_calculator.new_add('') == 0

def test_no_negetive():
    with pytest.raises(Exception, match = r'negatives not allowed \[-1, -2, -3\]'):
        string_calculator.new_add('-1, -2, -3, 1, 2, 3')

def test_new_sum():
    #test the sum with index
    # 0 index will be countest as even
    # Sum even index = 1 + 3
    # Sum odd index = 2 + 4
    # Returns = even - odd : 4 - 6 == -2 
    assert string_calculator.new_add("1,2,3,4") == -2

def test_add_two_numbers1():
    # it should test 2 numbers
    print("Testing 2 numbers in string")
    assert string_calculator.new_add('1, 2') == -1

def test_add_multiple_numbers1():
	# it should test multiple numbers
    print("Testing multiple numbers in string")
    assert string_calculator.new_add('1, 2, 3') == 2

def test_add_new_line_character1():
	# it should test new line character in number string
    print("Testing new line character in string")
    assert string_calculator.new_add('1\n2,3') == 2

def test_add_diff_delimeters1():
	# it should test different delimeters in string
    print("Testing different delimeters in string")
    assert string_calculator.new_add("//;\n1;2") == -1

def test_sample():
    # 2,2,2,3
    # 4 - 5 = -1
    # 6 - 3 = 3
    assert string_calculator.new_add("2,2,2,3") == -1
