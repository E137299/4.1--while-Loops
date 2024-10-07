from main import *

def test_sum_to_n():
    assert sum_to_n(5) == 15
    assert sum_to_n(6) == 21
    assert sum_to_n(7) == 28

def test_even_numbers():
    assert even_numbers(7,9) == "8 "
    assert even_numbers(3, 10) == "4 6 8 10 "

def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(5) == True
    assert is_prime(21) == False

def test_number_to_names():
    assert number_to_names(123) == "one two three"
    assert number_to_names(100) == "one zero zero"