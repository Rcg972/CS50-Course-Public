from twttr import shorten


def test_UCase():
    assert shorten("ANJAY GURINJAY") == "NJY GRNJY"


def test_LCase():
    assert shorten("gile lu ndro") == "gl l ndr"

def test_number():
    assert shorten("Taufik1224") == "Tfk1224"

def test_tanda():
    assert shorten("GELOOOOO!!!") == "GL!!!"


