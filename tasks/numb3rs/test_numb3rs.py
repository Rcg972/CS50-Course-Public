from numb3rs import validate


def test_ip():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False

def test_str():
    assert validate("cat") == False
    assert validate("dog") == False
    assert validate("123456") == False
    assert validate("255255255255") == False
