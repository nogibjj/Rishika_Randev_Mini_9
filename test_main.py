from main import add


def test_add():
    """testing out add function"""
    assert add(3, 10) == 13
    assert add(2, -2) == 0
    assert add(5, 6) == 11


if __name__ == "__main__":
    test_add()
