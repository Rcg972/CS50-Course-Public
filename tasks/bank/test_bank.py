from bank import value

def test_return_zero():
    assert value("hello gais") == 0
    assert value("HELLO GAIS") == 0
    assert value("Hello, world") == 0

def test_return_twenty():
    assert value("harimau putih") == 20
    assert value("Harimau Putih") == 20

def test_return_one_hundred():
    assert value("Anjay mabar") == 100
    assert value("Good morning") == 100



