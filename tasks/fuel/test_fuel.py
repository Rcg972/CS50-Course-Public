from fuel import convert, gauge
import pytest

def test_convert_benar():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25


def test_convert_salah():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

    with pytest.raises(ValueError):
        convert("-1/4")



def test_gaugee():
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
