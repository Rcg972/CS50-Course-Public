from plates import is_valid


def test_Two_Letters():
    assert is_valid("AB") == True
    assert is_valid("A")  == False
    assert is_valid("12") == False

def test_max_char():
    assert is_valid("AAABBB") == True
    assert is_valid("AAABBBC") == False
    assert is_valid("123456") == False

def test_num_in_mid():
    assert is_valid("AAAB12") == True
    assert is_valid("AA23BB") == False

def test_punctuation_and_spaces():
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("PI3.14") == False

def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False




