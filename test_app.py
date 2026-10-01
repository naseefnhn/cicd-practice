from app import add

def test_add():
    assert add(2, 3) == 10

def test_add_negative():
    assert add(-2, -3) == -5